"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy_head = Node(0)
        prev = dummy_head

        stack = [head]
        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev
            prev = curr

            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None

        dummy_head.next.prev = None
        return dummy_head.next
            

        