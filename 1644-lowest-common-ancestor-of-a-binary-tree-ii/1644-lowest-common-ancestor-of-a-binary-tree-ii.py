# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: 'TreeNode', targetNode: 'TreeNode') -> bool:
            if node is None:
                return False
            
            if node == targetNode:
                return True
            
            return dfs(node.left, targetNode) or dfs(node.right, targetNode)

        if root is None:
            return None
        
        if root == p and dfs(root, q) or root == q and dfs(root, p) or dfs(root.left, p) and dfs(root.right, q) or dfs(root.right, p) and dfs(root.left, q):
            return root
        
        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(root.right, p, q)
