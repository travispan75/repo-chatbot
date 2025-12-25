import simpleGit from "simple-git";
import { createHash } from "crypto";
import fs from "fs";
import { redis } from "@/lib/redis";
import path from "path";

type LoadRepoBody = {
    url: string;
};

function normalizeRepoUrl(raw: string): string {
    const u = new URL(raw);
    u.protocol = "https:";
    u.search = "";
    u.pathname = u.pathname.replace(/\/+$/, "");
    u.pathname = u.pathname.replace(/\.git$/, "");

    return u.toString();
}

export async function POST(request: Request) {
    const body = await request.json() as LoadRepoBody;
    let git_repo_url;

    try {
        git_repo_url = normalizeRepoUrl(body.url);
    } catch (e) {
        return Response.json({ error: "invalid url" }, { status: 400 });
    }

    const id = createHash("sha1").update(git_repo_url).digest("hex");
    const parentPath = path.join(process.cwd(), "data", "repos");
    const repoPath = path.join(parentPath, id);

    if (fs.existsSync(repoPath)) {
        const gitRepo = simpleGit(repoPath);
        await gitRepo.pull();
    } else {
        const gitParent = simpleGit(parentPath);
        await gitParent.clone(git_repo_url, id);
    }

    await redis.lpush(
        "repo_jobs",
        JSON.stringify({
            job_id: id,
            repo_path: repoPath,
            repo_url: git_repo_url,
        })
    );

    return Response.json({ status: 200 });
}