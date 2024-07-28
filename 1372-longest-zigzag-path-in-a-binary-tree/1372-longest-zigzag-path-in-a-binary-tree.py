# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxLength = 0

        def traversal(node: Optional[TreeNode], isLeft: bool, length: int) -> None:
            if node is None:
                return
            
            self.maxLength = max(self.maxLength, length)
            
            if isLeft:
                traversal(node.right, False, length + 1)
                traversal(node.left, True, 1)
            else:
                traversal(node.left, True, length + 1)
                traversal(node.right, False, 1)
        
        traversal(root, True, 0)
        traversal(root, False, 0)
        
        return self.maxLength