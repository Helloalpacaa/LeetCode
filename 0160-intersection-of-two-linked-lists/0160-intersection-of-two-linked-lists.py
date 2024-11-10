# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = 0
        lengthB = 0
        curr = headA
        while curr:
            lengthA += 1
            curr = curr.next
        curr = headB
        while curr:
            lengthB += 1
            curr = curr.next
        
        if lengthB < lengthA:
            return self.getIntersectionNode(headB, headA)
        
        curr = headB
        for _ in range(lengthB - lengthA):
            curr = curr.next
        
        currA = headA
        currB = curr
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        
        return None
