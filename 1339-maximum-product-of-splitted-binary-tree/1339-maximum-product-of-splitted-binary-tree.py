# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            currSum = node.val + traversal(node.left) + traversal(node.right)

            self.sums.append(currSum)

            return currSum

        self.sums = []
        total = traversal(root)
        
        max_product = 0
        for sum in self.sums:
            max_product = max(max_product, sum * (total - sum))

        return max_product % (10 ** 9 + 7)
        
        