# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def traverse(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1
            
            left = traverse(node.left) + 1
            right = traverse(node.right) + 1
            # print(node.val, left, right)
            self.diameter = max(self.diameter, left + right)

            return max(left, right)
        
        traverse(root)
        return self.diameter