# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(left, right) -> bool:
            if left and right:
                return left.val == right.val and isSame(left.left, right.left) and isSame(left.right, right.right)
            elif left is None and right is None:
                return True
            else:
                return False
        
        if not root:
            return False
        
        if isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)