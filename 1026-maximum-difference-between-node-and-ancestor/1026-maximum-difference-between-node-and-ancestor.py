# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def traversal(node: Optional[TreeNode], minVal: int, maxVal: int) -> int:
            if node is None:
                return maxVal - minVal
            
            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            return max(traversal(node.left, minVal, maxVal), traversal(node.right, minVal, maxVal))
        
        return traversal(root, root.val, root.val)