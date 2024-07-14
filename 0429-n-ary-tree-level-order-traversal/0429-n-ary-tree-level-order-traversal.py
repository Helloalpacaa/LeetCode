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
        self.traversal(root, 0, ans)
        return ans
        
    def traversal(self, node: 'Node', height: int, ans: List[List[int]]) -> None:
        if node is None:
            return
        
        if height >= len(ans):
            ans.append([])
        
        ans[height].append(node.val)
        for child in node.children:
            self.traversal(child, height + 1, ans)
            