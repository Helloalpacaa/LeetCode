# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 and node2:
                return node1.val == node2.val and isSame(node1.left, node2.right) and isSame(node1.right, node2.left)
            
            return not node1 and not node2
        
        if root is None:
            return True
        
        return isSame(root.left, root.right)