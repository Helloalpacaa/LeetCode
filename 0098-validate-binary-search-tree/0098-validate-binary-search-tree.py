# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], floor, ceiling) -> bool:
            if node is None:
                return True
            
            if node.val <= floor or node.val >= ceiling:
                return False
            
            # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
            return isValid(node.left, floor, node.val) and isValid(node.right, node.val, ceiling)
        
        return isValid(root.left, -float(inf), root.val) and isValid(root.right, root.val, float(inf))