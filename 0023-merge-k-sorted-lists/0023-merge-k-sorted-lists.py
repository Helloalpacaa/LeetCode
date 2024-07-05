# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, listHead in enumerate(lists):
            if listHead: # 这个条件必须加，因为可能有empty的list
                # listHead.val is used for comparison
                # i is used as a tie-breaker if two nodes have the same value
                # listHead is the actual node
                heapq.heappush(minHeap, (listHead.val, i, listHead))
        
        dummy = ListNode(0)
        curr = dummy
        
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            
            if curr.next:
                heapq.heappush(minHeap, (curr.next.val, i, curr.next))
        
        return dummy.next