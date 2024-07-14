# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        self.traversal(root, 0)
        
        return self.maxDepth
    
    def traversal(self, node: Optional[TreeNode], height: int) -> None:
        if node is None:
            return
        
        self.maxDepth = max(self.maxDepth, height + 1)
        self.traversal(node.left,height + 1)
        self.traversal(node.right, height + 1)