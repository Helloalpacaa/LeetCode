# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        ans = root.val
        
        def traverse(node: Optional) -> None:
            nonlocal ans
            if node is None:
                return
            
            traverse(node.left)
            arr.append(node.val)
            if len(arr) == k:
                ans = arr[-1]
                return
            traverse(node.right)
        
        traverse(root)
        return ans