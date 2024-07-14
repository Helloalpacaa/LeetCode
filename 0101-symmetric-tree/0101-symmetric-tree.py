# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root.left, root.right)
    
    def isSame(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 and node2:
            return node1.val == node2.val and self.isSame(node1.left, node2.right) and self.isSame(node1.right, node2.left)
        else:
            return node1 is None and node2 is None