class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        left = 0
        right = nums[-1] - nums[0]

        while left <= right:
            mid = (left + right) // 2
            count = 0

            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                
                count += j - i - 1
            
            if count < k: # 完全不满足条件的情况，count必须大于等于k，太小的话说明mid的值太小，需要加大left
                left = mid + 1
            else:
                right = mid - 1
        
        return left

