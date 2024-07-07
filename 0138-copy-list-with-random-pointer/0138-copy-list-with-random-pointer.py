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
        # First ietration, make a copy node of each original node, insert the copy node into linked list just follow the original node
        curr = head
        while curr:
            copy = Node(curr.val, None, None)
            n = curr.next
            copy.next = n
            curr.next = copy
            curr = curr.next.next
        
        # Second ietration, assign the random pointer to the copy node
        curr = head
        while curr:
            copy = curr.next
            random = curr.random.next if curr.random else None
            copy.random = random
            curr = curr.next.next
        
        # extract the copy linked list and retrive the original linked list
        curr = head
        dummy = Node(0)
        copy = dummy
        while curr:
            copy.next = curr.next
            curr.next = curr.next.next
            copy = copy.next
            curr = curr.next
        
        return dummy.next
        
        
        
            