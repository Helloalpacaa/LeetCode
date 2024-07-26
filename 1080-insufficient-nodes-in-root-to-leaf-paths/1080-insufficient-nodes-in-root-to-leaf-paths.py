# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if not root.left and not root.right:
            return root if root.val >= limit else None
        
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)

        # 来到这里说明这个node本来不是leaf，但是left和right child被改为了None
        return None if not root.left and not root.right else root