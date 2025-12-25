from steps.BaseStep import BaseStep
from context import Context

class BuildFileTreeStep(BaseStep):
    def __init__(self):
        pass
    
    def __dfs_build(self, root: str, entry_by_path: dict, adj_list: dict) -> dict:
        tree_node = {
            "path": root,
            "name": entry_by_path[root]["name"],
            "is_dir": entry_by_path[root]["is_dir"],
        }
        if tree_node["is_dir"]:
            tree_node["children"] = []
            for child in adj_list.get(root, []):
                tree_node["children"].append(self.__dfs_build(child, entry_by_path, adj_list))
        return tree_node
        
    def run(self, ctx: Context) -> None:
        ctx.repo_tree = self.__dfs_build('.', ctx.entry_by_path, ctx.adjacency_list)