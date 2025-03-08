class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        ones = 0

        for num in nums:
            if num == 0:
                ones = 0
            else:
                ones += 1
            ans = max(ans, ones)
        
        return ans