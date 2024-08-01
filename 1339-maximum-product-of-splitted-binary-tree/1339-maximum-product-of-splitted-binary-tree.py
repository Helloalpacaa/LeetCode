# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def sumCal(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            self.total += node.val
            sumCal(node.left)
            sumCal(node.right)
        
        sumCal(root)
        self.maxPro = float('-inf')

        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = traversal(node.left)
            right = traversal(node.right)

            currSum = left + right + node.val
            self.maxPro = max(self.maxPro, currSum * (self.total - currSum))

            return currSum

        traversal(root)
        return self.maxPro % (10 ** 9 + 7)