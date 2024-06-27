# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr is not None:
            nextNode = curr.next
            while nextNode and nextNode.val == curr.val:
                nextNode = nextNode.next
            curr.next = nextNode
            curr = curr.next
        
        return head