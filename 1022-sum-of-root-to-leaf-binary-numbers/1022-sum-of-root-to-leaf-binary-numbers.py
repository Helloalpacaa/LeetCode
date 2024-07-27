# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def traversal(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            
            val += node.val
            left = traversal(node.left, val * 2)
            right = traversal(node.right, val * 2)
            
            if node.left is None and node.right is None:
                self.ans += val + left + right
            
            return val + left + right
        
        traversal(root, 0)
        return self.ans