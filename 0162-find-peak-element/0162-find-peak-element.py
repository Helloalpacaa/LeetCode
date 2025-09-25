class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        candidates = {i for i in range(1, n) if nums[i] > nums[i - 1]}

        if n - 1 in candidates:
            return n - 1
        if nums[0] > nums[1]:
            return 0
        
        for i in range(n - 2, 0, -1):
            if i in candidates and nums[i] > nums[i + 1]:
                return i
        
        return 0