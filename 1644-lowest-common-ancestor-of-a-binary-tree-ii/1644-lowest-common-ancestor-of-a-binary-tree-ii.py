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

        def traversal(node: 'TreeNode') -> 'TreeNode':
            if node is None:
                return None
            
            left = traversal(node.left)
            right = traversal(node.right)
            
            if node == p:
                self.p_found = True
                return p

            if node == q:
                self.q_found = True
                return q
            
            if left and right:
                return node
            
            return left or right
        
        ans = traversal(root)
        return ans if self.p_found and self.q_found else None
