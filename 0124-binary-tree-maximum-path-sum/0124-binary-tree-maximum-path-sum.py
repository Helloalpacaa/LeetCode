# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')

        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = max(traversal(node.left), 0)
            right = max(traversal(node.right), 0)

            self.maxPath = max(self.maxPath, node.val + left + right)

            return node.val + max(left, right)
        
        traversal(root)
        return self.maxPath