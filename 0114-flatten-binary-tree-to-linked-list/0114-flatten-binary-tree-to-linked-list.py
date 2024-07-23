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

        # 先从3开始，3是一个点，就是一条直线，再到4，再返回到上一层2，把234连成一条直线
        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root
        while p.right:
            p = p.right
        p.right = right


        