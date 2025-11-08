# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        prev = None
        
        def dfs(node: TreeNode) -> bool:
            nonlocal prev

            if not node:
                return True
            
            left = dfs(node.left)
            if prev is not None and node.val <= prev:
                return False
            prev = node.val
            right = dfs(node.right)

            return left and right

        return dfs(root)
