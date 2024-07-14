# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()
        
        if root:
            queue.append(root)
        
        while queue:
            size = len(queue)
            maxValue = -float('inf')
            while size > 0:
                tmp = queue.popleft()
                if tmp.val > maxValue:
                    maxValue = tmp.val
                
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                size -= 1
            ans.append(maxValue)
        
        return ans