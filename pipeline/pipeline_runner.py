from steps.BuildFileTreeStep import BuildFileTreeStep
from steps.BuildPathTableStep import BuildPathTableStep
from steps.ClassifyFilesStep import ClassifyFilesStep
from steps.LoadFileContentsStep import LoadFileContentsStep
from steps.ParseSyntaxTreesStep import ParseSyntaxTreesStep
from steps.ScanFilesStep import ScanFilesStep

from context import Context

class Pipeline:
    steps = (
        ScanFilesStep(),
        ClassifyFilesStep(),
        BuildPathTableStep(),
        BuildFileTreeStep(),
        LoadFileContentsStep(),
        ParseSyntaxTreesStep(),
    )
    def run(self, repo_path: str):
        ctx = Context(repo_path=repo_path)
        for step in self.steps:
            step.run(ctx)
        ctx._debug_print(debug_repo_path=True, debug_counts=True, debug_keys=True, debug_repo_tree=True)