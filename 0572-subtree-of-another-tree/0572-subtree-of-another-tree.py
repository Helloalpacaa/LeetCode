# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if node1 and node2:
            return node1.val == node2.val and self.isSame(node1.left, node2.left) and self.isSame(node1.right, node2.right)
        else:
            return node1 is None and node2 is None