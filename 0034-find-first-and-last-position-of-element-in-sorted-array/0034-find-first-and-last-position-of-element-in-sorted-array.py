class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                start = mid
                while start - 1 >= 0 and nums[start - 1] == nums[start]:
                    start -= 1
                end = mid
                while end + 1 < len(nums) and nums[end + 1] == nums[end]:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [-1, -1]