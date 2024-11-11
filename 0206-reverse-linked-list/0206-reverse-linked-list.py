# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        prev, curr, next_node = None, head, head.next
        while curr:
            curr.next, next_node = prev, curr.next
            prev, curr = curr, next_node

        
        return prev
        