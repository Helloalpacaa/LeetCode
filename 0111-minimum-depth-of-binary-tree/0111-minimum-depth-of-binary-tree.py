# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.minDepth = float('inf')
        self.traversal(root, 0)
        
        return 0 if self.minDepth == float('inf') else self.minDepth
    
    def traversal(self, node: Optional[TreeNode], height: int) -> None:
        if node is None:
            return
        
        if node.left is None and node.right is None:
            self.minDepth = min(self.minDepth, height + 1)
        
        self.traversal(node.left, height + 1)
        self.traversal(node.right, height + 1)