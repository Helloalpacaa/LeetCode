# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def traversal(node: Optional[TreeNode], val: int) -> None:
            if node is None:
                return
            
            val = val * 10 + node.val

            if not node.left and not node.right:
                self.ans += val
            
            traversal(node.left, val)
            traversal(node.right, val)
        
        traversal(root, 0)
        return self.ans