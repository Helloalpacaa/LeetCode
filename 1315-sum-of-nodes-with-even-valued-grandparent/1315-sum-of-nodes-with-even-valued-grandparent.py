# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0

        def traversal(node: TreeNode, parent: TreeNode, grandparent: TreeNode) -> None:
            if node is None:
                return
            
            if grandparent and grandparent.val % 2 == 0:
                self.ans += node.val
            
            traversal(node.left, node, parent)
            traversal(node.right, node, parent)
        
        traversal(root, None, None)
        return self.ans
            

