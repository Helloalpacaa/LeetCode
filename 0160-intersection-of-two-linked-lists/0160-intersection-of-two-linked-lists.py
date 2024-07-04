# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        currA = headA
        while currA:
            sizeA += 1
            currA = currA.next
            
        sizeB = 0
        currB = headB
        while currB:
            sizeB += 1
            currB = currB.next
        
        currA = headA
        currB = headB
        while sizeA > sizeB:
            currA = currA.next
            sizeA -= 1
        while sizeB > sizeA:
            currB = currB.next
            sizeB -= 1
        
        while currA != currB:
            currA = currA.next
            currB = currB.next
        
        return currA
        