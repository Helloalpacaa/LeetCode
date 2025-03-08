# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        # if root is None:
        #     return ans
        
        # queue = deque([root])

        # while queue:
        #     ans.append(queue[0].val)
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         if node.right:
        #             queue.append(node.right)
        #         if node.left:
        #             queue.append(node.left)
        
        # return ans

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if node is None:
                return
            
            if len(ans) < depth:
                ans.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 1)
        return ans