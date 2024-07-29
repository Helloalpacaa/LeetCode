# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxBST = 0

        # return is_BST, minVal, maxVal, sumVal
        def traversal(node: Optional[TreeNode]):
            if node is None:
                return True, float('inf'), float('-inf'), 0
            
            left_isBST, left_minVal, left_maxVal, left_sumVal = traversal(node.left)
            right_isBST, right_minVal, right_maxVal, right_sumVal = traversal(node.right)

            if left_isBST and right_isBST and left_maxVal < node.val < right_minVal:
                sumVal = left_sumVal + right_sumVal + node.val
                self.maxBST = max(self.maxBST, sumVal)
                minVal = min(left_minVal, node.val)
                maxVal = max(right_maxVal, node.val)
                return True, minVal, maxVal, sumVal
            
            return False, 0, 0, 0
        
        traversal(root)
        return self.maxBST
        
