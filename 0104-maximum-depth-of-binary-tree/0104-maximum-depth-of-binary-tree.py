# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0

        def traversal(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            
            depth += 1
            if node.left is None and node.right is None:
                self.maxDepth = max(self.maxDepth, depth)

            traversal(node.left, depth)
            traversal(node.right, depth)
        
        traversal(root, 0)
        return self.maxDepth