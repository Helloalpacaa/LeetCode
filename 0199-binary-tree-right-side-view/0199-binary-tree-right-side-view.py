# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            level_size = len(queue)
            ans.append(queue[0].val)
            while level_size > 0:
                tmp = queue.popleft()
                if tmp.right:
                    queue.append(tmp.right)
                if tmp.left:
                    queue.append(tmp.left)
                level_size -= 1
        
        return ans