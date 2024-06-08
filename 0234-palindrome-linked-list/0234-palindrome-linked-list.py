# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # slow此时在中点
        
        # 反转从slow到fast这部分
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        
        fast, slow = head, prev
        
        while slow:
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next
            
        return True
            
            
        