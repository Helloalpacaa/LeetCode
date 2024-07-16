"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.maxDepth = 0
        self.traversal(root, 0)
        
        return self.maxDepth
    
    def traversal(self, node: 'Node', height: int) -> None:
        if node is None:
            return
        
        self.maxDepth = max(self.maxDepth, height + 1)
        for child in node.children:
            self.traversal(child, height + 1)