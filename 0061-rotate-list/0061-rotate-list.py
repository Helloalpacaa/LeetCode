# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        curr = dummy
        size = 0
        while curr.next:
            size += 1
            curr = curr.next
        tail = curr # get the size of the linked list, get the tail node
        
        tail.next = head # generate a circle
        
        for _ in range((size - k) % size):
            tail = tail.next
        
        newHead = tail.next
        tail.next = None
        
        return newHead
