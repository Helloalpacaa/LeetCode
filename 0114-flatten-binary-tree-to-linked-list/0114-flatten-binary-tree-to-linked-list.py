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
        if not root:
            return

        stack = []

        def traversal(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            traversal(node.right)
            traversal(node.left)
            stack.append(node)
            # post order: 6, 5, 4, 3, 4, 2, 1
        
        traversal(root)
        dummy = TreeNode(0)
        curr = dummy
        while stack:
            curr.right = stack.pop()
            curr.left = None
            curr = curr.right


        

            
            
        
