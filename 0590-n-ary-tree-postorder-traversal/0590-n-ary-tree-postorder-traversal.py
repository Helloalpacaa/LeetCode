"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.traversal(root, ans)
        ans.append(root.val) if root is not None else None
        return ans
    
    def traversal(self, node: 'Node', ans: List[int]) -> None:
        if node is None:
            return
        
        for child in node.children:
            self.traversal(child, ans)
            ans.append(child.val)