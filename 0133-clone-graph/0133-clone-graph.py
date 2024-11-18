"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        # 建立一个hashmap存储value: node，key: clone
        # 把1 clone以后去clone它的neighbor 2, 2的neighbor里又会包含1，又回到了1，这时候直接return clone的1不需要再去clone 1以及它的neighbor
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        if node in self.visited:
            return self.visited[node]

        clone = Node(node.val, [])
        self.visited[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        
        return clone