# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, slow, prev.next = slow, slow.next, None
        
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        tail = prev
        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        
        return True
            