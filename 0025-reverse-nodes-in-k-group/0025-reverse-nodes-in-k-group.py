# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a, b = head, head
        
        for _ in range(k):
            if not b:
                return head
            b = b.next
        
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
    
    
    def reverse(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        pre, curr = None, a
        while curr != b:
            nex = curr.next
            curr.next = pre
            pre = curr
            curr = nex
        
        return pre
                
            