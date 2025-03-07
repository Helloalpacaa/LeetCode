# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            
            if len(ans) < depth:
                ans.append([])
            
            ans[depth - 1].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        return ans