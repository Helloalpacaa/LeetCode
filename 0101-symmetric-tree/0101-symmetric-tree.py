# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSame(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            elif node1 and node2:
                if node1.val != node2.val:
                    return False
                return isSame(node1.left, node2.right) and isSame(node1.right, node2.left)
            else:
                return False
        
        return isSame(root.left, root.right)