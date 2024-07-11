# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        prev, curr, prev.next = slow, slow.next, None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        left = head
        right = prev
        
        while left and right and left != right:
            right.next, left.next, left, right = left.next, right, left.next, right.next
        left.next = None
        
        
        