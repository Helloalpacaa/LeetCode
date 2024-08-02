# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum = 0

        # return isBST, minVal, maxVal, currSum
        def traversal(node: Optional[TreeNode]) -> (bool, float, float, int):
            if node is None:
                return True, float('inf'), float('-inf'), 0
            
            left_isBST, left_minVal, left_maxVal, left_sum = traversal(node.left)
            right_isBST, right_minVal, right_maxVal, right_sum = traversal(node.right)

            if left_isBST and right_isBST and left_maxVal < node.val < right_minVal:
                curr_sum = left_sum + right_sum + node.val
                self.maxSum = max(self.maxSum, curr_sum)
                return True, left_minVal if node.left else node.val, right_maxVal if node.right else node.val, curr_sum
            
            return False, 0, 0, 0
        
        traversal(root)
        return self.maxSum
