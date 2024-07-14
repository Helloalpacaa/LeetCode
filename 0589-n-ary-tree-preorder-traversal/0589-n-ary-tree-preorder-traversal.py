"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.traversal(root, ans)
        return ans
        
    
    def traversal(self, node: 'Node', ans: List[int]) -> None:
        if node is None:
            return
        
        ans.append(node.val)
        for child in node.children:
            self.traversal(child, ans)