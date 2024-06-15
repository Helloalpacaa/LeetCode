class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minHeap = [] # store the tuple(value, index) into a minHeap
        maxHeap = [] # store the tuple(value, index) into a maxHeap  

        i = 0
        ans = 0
        for j in range(len(nums)):
            heapq.heappush(minHeap, (nums[j], j))
            heapq.heappush(maxHeap, (-nums[j], j))
            
            # compare max - min with limit
            while -maxHeap[0][0] - minHeap[0][0] > limit:
                # move i to the new start of a valid sliding window
                i = min(minHeap[0][1], maxHeap[0][1]) + 1
                
                # pop all the elements before nums[i]
                while minHeap[0][1] < i:
                    heapq.heappop(minHeap)
                while maxHeap[0][1] < i:
                    heapq.heappop(maxHeap)
            
            ans = max(ans, j - i + 1)
        
        return ans
        