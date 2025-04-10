class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0

        product = 1
        left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1

            count += (right - left + 1)
        
        return count