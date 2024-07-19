# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        maxValue = max(nums)
        maxIdx = nums.index(maxValue)
        
        root = TreeNode(maxValue)
        root.left = self.constructMaximumBinaryTree(nums[0: maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx + 1: len(nums)])
        
        return root