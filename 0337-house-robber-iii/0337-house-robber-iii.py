# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # return a tuple(rob, not_rob)
        def dfs(node: Optional[TreeNode]) -> (int, int):
            if node is None:
                return 0, 0
            
            # 后序遍历，因为我们要先拿到left和right的结果
            left = dfs(node.left)
            right = dfs(node.right)

            # 抢当前node，那么就不能抢left child and right child
            rob = node.val + left[1] + right[1]
            # 不抢当前node，就可以抢left child and right child，可以选择抢或者不抢，取更大的值
            not_rob = max(left) + max(right)

            return (rob, not_rob)
        
        return max(dfs(root))