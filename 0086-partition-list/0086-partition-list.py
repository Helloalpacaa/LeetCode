# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0, head) # to traverse the original linked list
        dummy2 = ListNode(None) # to generate a new linked list with all the nodes < x
        curr1 = dummy1
        curr2 = dummy2
        
        while curr1.next:
            if curr1.next.val < x:
                curr2.next = curr1.next
                curr1.next = curr1.next.next
                curr2 = curr2.next
            else:
                curr1 = curr1.next
        
        curr2.next = dummy1.next
        return dummy2.next