# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = 0
        left = root.left
        while left:
            leftHeight += 1
            left = left.left
            
        rightHeight = 0
        right = root.right
        while right:
            right = right.right
            rightHeight += 1
        
        if leftHeight == rightHeight:
            return 2 ** (leftHeight + 1) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)