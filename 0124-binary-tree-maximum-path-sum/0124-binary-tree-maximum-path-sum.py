# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            # 只考虑结果不为负数的subtree，如果结果为负数，就不把这个subtree计算进来
            left = max(traversal(node.left), 0)
            right = max(traversal(node.right), 0)

            # 更新最大值时，只考虑经过了这个node的，因为不经过的情况，在subtree里已经考虑过，而如果subtree为负数，也不会被考虑进来
            self.maxSum = max(self.maxSum, left + right + node.val)

            # 向上返回经过了当前node的最大path，不能是left+right，只能选一条边往上返回
            return node.val + max(left, right)
        
        traversal(root)
        return self.maxSum
