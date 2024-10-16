class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Sliding Window + Heap
        window = Counter(nums[:k])

        def getSum():
            heap = [(-freq, -num) for num, freq in window.items()]
            heapq.heapify(heap)
            total = 0
            for _ in range(min(x, len(heap))):
                freq, num = heapq.heappop(heap)
                total += -freq * -num

            return total
        
        ans = []
        ans.append(getSum())

        for i in range(k, len(nums)):
            window[nums[i - k]] -= 1
            if window[nums[i - k]] == 0:
                del window[nums[i - k]]
            
            window[nums[i]] += 1

            ans.append(getSum())
        
        return ans
