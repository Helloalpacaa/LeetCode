# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.maxAve = float('-inf')
        self.count = 0

        def traversal(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            
            left = traversal(node.left, val)
            right = traversal(node.right, val)

            val = node.val + left + right
            self.count += 1
            print(val)
            self.maxAve = max(self.maxAve, val / self.count)

            return val
        
        traversal(root, 0)
        return self.maxAve
            
