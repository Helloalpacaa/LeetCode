# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_found = False
        self.q_found = False

        def dfs(node: 'TreeNode') -> 'TreeNode':
            if node is None:
                return None
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node == p:
                self.p_found = True
                return node
            
            if node == q:
                self.q_found = True
                return node
            
            if left and right:
                return node
            
            return left or right

        result = dfs(root)

        if self.p_found and self.q_found:
            return result
        else:
            return None
