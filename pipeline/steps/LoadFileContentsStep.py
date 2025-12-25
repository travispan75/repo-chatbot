from steps.BaseStep import BaseStep
from context import Context
import os

class LoadFileContentsStep(BaseStep):
    def __init__(self):
        pass
    
    def run(self, ctx: Context) -> None:
        ctx.file_contents = {}
        repo_path = ctx.repo_path

        for entry in ctx.repo_entries:
            if entry["category"] == "source_code":
                rel = entry["rel_path"]
                full_path = os.path.join(repo_path, rel)

                try:
                    with open(full_path, "rb") as f:
                        ctx.file_contents[rel] = f.read()
                except Exception:
                    ctx.file_contents[rel] = None