# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # stack = []
        # prev = float('-inf')

        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
            
        #     root = stack.pop()
        #     if root.val <= prev:
        #         return False
        #     prev = root.val
        #     root = root.right
        
        # return True
        self.prev = None
        
        def traverse(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            
            left = traverse(node.left)

            if self.prev is not None and node.val <= self.prev:
                return False
            
            self.prev = node.val
            right = traverse(node.right)

            return left and right
        
        return traverse(root)

        

        