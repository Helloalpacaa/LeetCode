class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap = []
        minHeap = []
        
        i = 0
        longest = 0
        for j in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[j], j))
            heapq.heappush(minHeap, (nums[j], j))
            
            if -maxHeap[0][0] - minHeap[0][0] > limit:
                i = min(minHeap[0][1], maxHeap[0][1]) + 1
                
                while minHeap[0][1] < i:
                    heapq.heappop(minHeap)
                while maxHeap[0][1] < i:
                    heapq.heappop(maxHeap)
            longest = max(longest, j - i + 1)
        
        return longest