# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        
        slow = head
        fast = head.next
        
        while fast is not None:
            if fast.val == slow.val:
                fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        
        slow.next = None
        
        return head