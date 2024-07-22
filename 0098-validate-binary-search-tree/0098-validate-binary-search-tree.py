# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node: Optional[TreeNode], low: int, high: int) -> bool:
            if node is None:
                return True
            
            if node.val >= high or node.val <= low:
                return False
            
            return inorder(node.left, low, node.val) and inorder(node.right, node.val, high)
        
        return inorder(root, -float('inf'), float('inf'))