# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return val
            
            val =  traversal(node.right, val)
            node.val += val
            
            return traversal(node.left, node.val)
        
        traversal(root, 0)
        return root