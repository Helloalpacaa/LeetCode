# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currA = list1
        currB = list2
        dummy = ListNode(0)
        curr = dummy
        
        while currA or currB:
            if not currA:
                curr.next = currB
                return dummy.next
            if not currB:
                curr.next = currA
                return dummy.next
            
            if currA.val <= currB.val:
                curr.next = currA
                currA = currA.next
            else:
                curr.next = currB
                currB = currB.next
            curr = curr.next
        
        return dummy.next
                