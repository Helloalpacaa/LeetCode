# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        def traversal(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            
            val += node.val
            if node.left is None and node.right is None:
                return val
            
            return traversal(node.left, val * 10) + traversal(node.right, val * 10)
        
        return traversal(root, 0)