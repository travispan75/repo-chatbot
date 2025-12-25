from steps.BaseStep import BaseStep
from context import Context

class ClassifyFilesStep(BaseStep):
    def __init__(self):
        pass

    def run(self, ctx: Context) -> None:
        ASSET_EXT = {
            "png","jpg","jpeg","gif","svg","webp",
            "mp4","mov","avi","mp3","wav","flac",
            "woff","woff2","ttf","eot"
        }

        BINARY_EXT = {
            "exe","dll","o","obj","so","pyc","class","wasm"
        }

        ARCHIVE_EXT = {
            "zip","tar","gz","bz2","7z","rar"
        }

        DOC_EXT = {"md","txt"}

        CONFIG_FILES = {
            "package.json",
            "requirements.txt",
            "dockerfile",
            "docker-compose.yml",
            ".gitignore",
        }

        ROOT_IGNORE_DIRS = {
            "node_modules",
            ".git",
        }

        for entry in ctx.repo_entries:
            name = entry["name"]
            rel = entry["rel_path"]
            ext = entry["ext"]
            lname = name.lower()

            if entry["is_dir"]:
                if "/" not in rel and rel in ROOT_IGNORE_DIRS:
                    entry["category"] = "ignored"
                else:
                    entry["category"] = "source_code"
            elif ext in ASSET_EXT:
                entry["category"] = "assets"
            elif ext in BINARY_EXT or ext in ARCHIVE_EXT:
                entry["category"] = "binaries"
            elif lname in CONFIG_FILES:
                entry["category"] = "config"
            elif "test" in lname or "spec" in lname:
                entry["category"] = "tests"
            elif ext in DOC_EXT:
                entry["category"] = "docs"
            else:
                entry["category"] = "source_code"
