# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def traversal(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = traversal(node.left)
            right = traversal(node.right)

            self.maxDiameter = max(self.maxDiameter, left + right)

            return max(left, right) + 1
        
        traversal(root)
        return self.maxDiameter