class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = float('-inf')
        total = 0

        i = 0
        for j in range(len(nums)):
            total += nums[j]

            if j - i + 1 > k:
                total -= nums[i]
                i += 1
            
            if j - i + 1 == k:
                max_average = max(max_average, total / k)
        
        return max_average
        