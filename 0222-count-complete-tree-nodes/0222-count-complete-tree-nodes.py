# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = root.left
        leftHeight = 0
        while left:
            leftHeight += 1
            left = left.left
        
        right = root.right
        rightHeight = 0
        while right:
            rightHeight += 1
            right = right.right
        
        if leftHeight == rightHeight:
            return 2 ** (leftHeight + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)