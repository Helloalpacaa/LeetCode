# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
            
        # 先把root的左边拉成一条直线，再把root的右边拉成一条直线
        self.flatten(root.left)
        self.flatten(root.right)

        # 从左下角开始，不断地把三角形拉成直线
        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root
        while p.right:
            p = p.right
        p.right = right


        