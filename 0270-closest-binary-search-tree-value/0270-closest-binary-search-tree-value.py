# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = root.val
        diff = abs(root.val - target)

        def traverse(node: Optional[TreeNode]) -> None:
            nonlocal ans, diff
            if node is None:
                return
            
            if abs(node.val - target) == diff:
                ans = min(ans, node.val)
            elif abs(node.val - target) < diff:
                ans = node.val
                diff = abs(node.val - target)
            
            if node.val > target:
                traverse(node.left)
            else:
                traverse(node.right)
        
        traverse(root)
        return ans