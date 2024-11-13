# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def isSame(left, right) -> bool:
            if left is None and right is None:
                return True
            elif left is not None and right is not None:
                return left.val == right.val and isSame(left.left, right.right) and isSame(left.right, right.left)
            else:
                return False
        
        return isSame(root.left, root.right)