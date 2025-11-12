class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left = [i for i in range(n)]

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                left[i] = i
            else:
                left[i] = left[i - 1]
        
        if left[n - 1] == n - 1:
            return n - 1
        
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1] and left[i] == i:
                return i
        
