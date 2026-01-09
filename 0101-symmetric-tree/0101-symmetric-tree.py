# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isSame(p, q) -> bool:
            if p and q:
                if p.val != q.val:
                    return False
                return isSame(p.left, q.right) and isSame(p.right, q.left)
            elif not p and not q:
                return True
            else:
                return False
        
        return isSame(root.left, root.right)