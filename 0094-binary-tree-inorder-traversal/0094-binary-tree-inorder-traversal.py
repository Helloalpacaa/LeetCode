# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            
            traversal(node.left)
            self.ans.append(node.val)
            traversal(node.right)

        self.ans = []
        traversal(root)

        return self.ans

