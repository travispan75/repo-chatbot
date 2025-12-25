from steps.BaseStep import BaseStep
from context import Context

class BuildPathTableStep(BaseStep):
    def __init__(self):
        pass

    def run(self, ctx: Context) -> None:
        for entry in ctx.repo_entries:
            ctx.entry_by_path[entry["rel_path"]] = entry
            ctx.files_by_category.setdefault(entry["category"], []).append(entry)   