# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return self.traversal(root, 0, targetSum)
    
    
    def traversal(self, node: Optional[TreeNode], total: int, targetSum: int) -> bool:
        if node is None:
            return False
        
        total += node.val
        
        if total == targetSum and node.left is None and node.right is None:
            return True
        
        return self.traversal(node.left, total, targetSum) or self.traversal(node.right, total, targetSum)
        