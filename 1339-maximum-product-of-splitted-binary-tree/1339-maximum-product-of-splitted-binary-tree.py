# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.product = float('-inf')
        self.total = 0

        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = traversal(node.left)
            right = traversal(node.right)
            currTotal = node.val + left + right

            if self.total:
                self.product = max(self.product, currTotal * (self.total - currTotal))

            return currTotal
        
        self.total = traversal(root)
        traversal(root)
        return self.product % (10 ** 9 + 7)
        
        