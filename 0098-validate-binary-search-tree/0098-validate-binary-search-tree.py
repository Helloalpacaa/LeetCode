# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            
            if not inorder(node.left):
                return False
            
            if self.pre is not None and node.val <= self.pre.val:
                return False
            
            self.pre = node

            return inorder(node.right)
        
        self.pre = None
        return inorder(root)