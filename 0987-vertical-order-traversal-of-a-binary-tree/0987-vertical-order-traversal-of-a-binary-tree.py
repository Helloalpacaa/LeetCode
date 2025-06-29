# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = [] # list of (col, row, value)
        
        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            if node is None:
                return
            
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        col_map = defaultdict(list)
        for col, row, value in sorted(nodes):
            col_map[col].append(value)
        
        return [col_map[x] for x in sorted(col_map)]
        