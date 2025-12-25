from steps.BaseStep import BaseStep
from context import Context
from tree_sitter_languages import get_parser

class ParseSyntaxTreesStep(BaseStep):
    def run(self, ctx: Context) -> None:
        EXT_TO_LANGUAGE = {
            ".sh": "bash",

            ".c": "c",
            ".h": "c",

            ".cpp": "cpp",
            ".cc": "cpp",
            ".cxx": "cpp",
            ".hpp": "cpp",
            ".hh": "cpp",

            ".css": "css",

            ".html": "html",
            ".htm": "html",

            ".go": "go",
            ".java": "java",
            ".rs": "rust",

            ".js": "javascript",
            ".mjs": "javascript",
            ".cjs": "javascript",

            ".ts": "typescript",
            ".tsx": "tsx",

            ".json": "json",
            ".yaml": "yaml",
            ".yml": "yaml",

            ".md": "markdown",
            ".markdown": "markdown",
            ".mdx": "markdown",

            ".py": "python",
        }

        parser_cache = {}

        for path, content in ctx.file_contents.items():
            if content:
                ext = ctx.entry_by_path[path]["ext"]

                if ext not in EXT_TO_LANGUAGE:
                    ctx.syntax_trees[path] = content.decode("utf-8", errors="replace")
                    continue

                language = EXT_TO_LANGUAGE[ext]

                if language not in parser_cache:
                    parser_cache[language] = get_parser(language)

                parser = parser_cache[language]
                tree = parser.parse(content)
                ctx.syntax_trees[path] = tree
