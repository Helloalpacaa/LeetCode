# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAverage = -float('inf')

        def traversal(node: Optional[TreeNode]) -> [int, float]:
            if node is None:
                return [0, 0.0]
            
            leftCounts, leftSum = traversal(node.left)
            rightCounts, rightSum = traversal(node.right)

            counts = leftCounts + rightCounts + 1
            total = leftSum + rightSum + node.val

            self.maxAverage = max(self.maxAverage, total / counts)

            return [counts, total]
            
        traversal(root)
        return self.maxAverage