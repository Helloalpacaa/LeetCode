"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        arr = []
        self.traversal(root, 0, arr)
        return root
    
    def traversal(self, node: 'Optional[Node]', height: int, arr: List[List[int]]) -> None:
        if node is None:
            return
        
        if height >= len(arr):
            arr.append([])
        else:
            arr[height][len(arr[height]) - 1].next = node
        
        arr[height].append(node)
        self.traversal(node.left, height + 1, arr)
        self.traversal(node.right, height + 1, arr)
        