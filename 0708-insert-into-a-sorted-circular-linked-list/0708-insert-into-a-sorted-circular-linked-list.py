"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)

        if head is None:
            newNode.next = newNode
            return newNode
        
        prev = head
        curr = head.next

        while prev.next != head:
            # Case1: 1 <- Node(2) <- 3
            if prev.val <= insertVal <= curr.val:
                break
            
            # Case2: 3 -> 1, 3 -> Node(4) -> 1, 3 -> Node(0) -> 1
            if prev.val > curr.val and (insertVal > prev.val or insertVal < curr.val):
                break
            
            prev = curr
            curr = curr.next
        
        prev.next = newNode
        newNode.next = curr

        return head



