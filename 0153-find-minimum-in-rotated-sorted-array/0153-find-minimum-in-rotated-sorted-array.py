class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]
            else:
                mid = (left + right) // 2
                if nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid
        