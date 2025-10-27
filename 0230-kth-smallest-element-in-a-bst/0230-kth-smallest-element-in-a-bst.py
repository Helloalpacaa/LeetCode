# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val

        def dfs(node: Optional[TreeNode]) -> None:
            nonlocal res, k

            if node is None:
                return
            
            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res