# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAve = 0
        
        def traversal(node: Optional[TreeNode]) -> Tuple[int, float]:
            if node is None:
                return [0, 0.0]
            
            leftCount, leftSum = traversal(node.left)
            rightCount, rightSum = traversal(node.right)

            total = node.val + leftSum + rightSum
            count = leftCount + rightCount + 1

            self.maxAve = max(self.maxAve, total / count)

            return (count, total)
        
        traversal(root)
        return self.maxAve
            
