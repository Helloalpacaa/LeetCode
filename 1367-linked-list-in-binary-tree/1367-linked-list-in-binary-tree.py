# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def traversal(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            if head is None:
                return True
            
            if root is None:
                return False
             
            if head.val != root.val:
                return False

            return traversal(head.next, root.left) or traversal(head.next, root.right)
        
        if head is None:
            return True
        if root is None:
            return False
        
        return traversal(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)