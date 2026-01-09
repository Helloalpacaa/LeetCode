# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstElement, secondElement, prevElement = None, None, None

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            nonlocal firstElement, secondElement, prevElement

            dfs(node.left)

            if not firstElement and prevElement and prevElement.val >= node.val:
                firstElement = prevElement
            
            if firstElement and prevElement.val >= node.val:
                secondElement = node
            
            prevElement = node

            dfs(node.right)
        
        dfs(root)
        firstElement.val, secondElement.val = secondElement.val, firstElement.val
            
