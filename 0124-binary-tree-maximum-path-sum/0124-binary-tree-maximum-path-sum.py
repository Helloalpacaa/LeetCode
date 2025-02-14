# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.maxPath = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.maxPath = max(self.maxPath, node.val + max(left, 0) + max(right, 0))

            return node.val + max(left, right, 0)
        
        dfs(root)
        return self.maxPath
