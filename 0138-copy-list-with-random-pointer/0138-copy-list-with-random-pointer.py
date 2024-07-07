"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        curr = head
        
        while curr:
            copy = Node(curr.val, None, None)
            hm[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            hm[curr].next = hm[curr.next] if curr.next else None
            hm[curr].random = hm[curr.random] if curr.random else None
            curr = curr.next
        
        return hm[head] if head else None
            