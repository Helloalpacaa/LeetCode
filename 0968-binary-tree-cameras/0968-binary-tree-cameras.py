# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            # 0: leaf node
            # 1: parent of leaf node, install camara here
            # 2: covered, no need to install camaera here
            if node is None:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                self.ans += 1
                return 1

            if left == 1 or right == 1:
                return 2

            return 0
        
        return (dfs(root) == 0) + self.ans