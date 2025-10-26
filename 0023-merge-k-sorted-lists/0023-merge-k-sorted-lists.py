# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        heap = []
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        prev = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            prev.next = node
            prev = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
