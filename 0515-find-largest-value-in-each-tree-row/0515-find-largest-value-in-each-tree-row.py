# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node: TreeNode, depth: int) -> None:
            if node is None:
                return
            
            if len(ans) <= depth:
                ans.append(node.val)
            
            if node.val > ans[depth]:
                ans[depth] = node.val
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
            return
        
        dfs(root, 0)
        return ans