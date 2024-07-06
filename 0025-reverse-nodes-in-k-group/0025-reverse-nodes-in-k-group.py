# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
            
        dummy = ListNode(0, head)
        p = dummy
        
        for _ in range(size // k):
            tail = p.next
            for _ in range(k - 1):
                tmp = p.next
                p.next = tail.next
                tail.next = tail.next.next
                p.next.next = tmp
            p = tail
        
        return dummy.next
                
            