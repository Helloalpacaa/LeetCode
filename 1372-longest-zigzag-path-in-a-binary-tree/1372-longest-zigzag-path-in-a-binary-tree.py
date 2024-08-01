# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def traversal(node: Optional[TreeNode], isLeft: bool, depth: int) -> None:
            if node is None:
                return

            # self.longest = max(self.longest, depth)

            if isLeft:
                traversal(node.right, False, depth + 1)
                traversal(node.left, True, 1)
            else:
                traversal(node.left, True, depth + 1)
                traversal(node.right, False, 1)
            
            self.longest = max(self.longest, depth)
            
        traversal(root, True, 0)
        traversal(root, False, 0)
        return self.longest