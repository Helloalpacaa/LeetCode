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
            node = queue.popleft()
            ans.append(node.val)
            size = len(queue)
            while size > 0:
                tmp = queue.popleft()
                if tmp.val > ans[len(ans) - 1]:
                    ans[len(ans) - 1] = tmp.val
                
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
                size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return ans