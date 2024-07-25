# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def traversal(node: Optional, val: int) -> int:
            if node is None:
                return 0
            
            val = val * 2 + node.val

            if node.left is None and node.right is None:
                return val
            
            return traversal(node.left, val) + traversal(node.right, val)
        
        return traversal(root, 0)