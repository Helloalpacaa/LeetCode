# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        # 0: leaf
        # 1: parents of leaves, should have camera
        # 2: covered
        # 我们只在leaf的parent放置camera
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                self.ans += 1
                return 1
            
            if left == 1 or right == 1:
                return 2
            
            # left == 2 or right == 2的情况不需要额外handle，这是node就相当于leaf，直接return 0
            return 0

        # adds 1 to the total if the root itself needs a camera
        return (dfs(root) == 0) + self.ans