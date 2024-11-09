class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums)
        # most_common = count.most_common(k)

        # ans = [item[0] for item in most_common]

        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for value, freq in count.items():
            heapq.heappush(heap, (freq, value))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = [item[1] for item in heap]

        return ans