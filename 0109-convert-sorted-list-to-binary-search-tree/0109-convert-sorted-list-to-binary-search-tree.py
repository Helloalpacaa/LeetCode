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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            curr = curr.next
        tail = curr

        def buildTree(start: Optional[ListNode], end: Optional[ListNode]) -> Optional[TreeNode]:
            if not start or not end:
                return None
            
            if start == end:
                return TreeNode(start.val)
            
            dummy = ListNode(0, start)
            slow, fast = dummy, dummy

            while slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            prev = slow
            rootNode = prev.next
            prev.next = None
            root = TreeNode(rootNode.val)
            root.left = buildTree(start, prev)
            root.right = buildTree(rootNode.next, end)

            return root
        
        return buildTree(head, tail)

