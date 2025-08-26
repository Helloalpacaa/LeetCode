# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        
        def traversal(node: TreeNode, count: int) -> (int, int):
            nonlocal ans
            if node is None:
                return (0, 0)
            
            left_val, left_count = traversal(node.left, count)
            right_val, right_count = traversal(node.right, count)
            total_val = left_val + right_val + node.val
            total_count = left_count + right_count + 1
            
            if total_val // total_count == node.val:
                ans += 1
                
            
            return (total_val, total_count)
        
        traversal(root, 0)
        return ans