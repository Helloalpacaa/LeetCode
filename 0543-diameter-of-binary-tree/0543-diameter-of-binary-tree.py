# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            left = height(node.left)
            right = height(node.right)
            self.maxDiameter = max(self.maxDiameter, left + right)

            return max(left, right) + 1
        
        self.maxDiameter = 0
        height(root)

        return self.maxDiameter