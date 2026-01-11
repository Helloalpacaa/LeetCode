# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        def getRoot(start: int, end: int) -> Optional[TreeNode]:
            if start > end:
                return None
            
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = getRoot(start, mid - 1)
            root.right = getRoot(mid + 1, end)

            return root
        
        return getRoot(0, n - 1)
