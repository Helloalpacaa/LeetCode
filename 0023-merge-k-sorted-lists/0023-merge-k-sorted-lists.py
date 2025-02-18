# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(0)
        curr = dummy
        while min_heap:
            value, index, node = heapq.heappop(min_heap)
            curr.next = ListNode(value)
            curr = curr.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))

        return dummy.next
