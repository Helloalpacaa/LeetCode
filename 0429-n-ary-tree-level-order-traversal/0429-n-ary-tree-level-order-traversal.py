"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        queue = deque()
        
        if root:
            queue.append(root)
            
        while queue:
            size = len(queue)
            ans.append([])
            while size > 0:
                node = queue.popleft()
                ans[len(ans) - 1].append(node.val)
                for child in node.children:
                    queue.append(child)
                size -= 1
        
        return ans
            