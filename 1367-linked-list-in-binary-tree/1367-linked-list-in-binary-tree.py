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
        if head is None:
            return True
         
        if root is None:
            return False
        
        #只比较当前node的结果
        def traversal(head: Optional[ListNode], node: Optional[TreeNode]) -> bool:
            if head is None:
                return True
            
            if node is None:
                return False
            
            if head.val != node.val:
                return False
            
            return traversal(head.next, node.left) or traversal(head.next, node.right)
        
        return traversal(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)