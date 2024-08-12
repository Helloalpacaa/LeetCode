class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 1. sort the array in ascending order
        nums.sort()

        # 2. flip the negative numbers
        i = 0
        while i < len(nums) and i < k and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
        
        # 3. count the sum, 不管k多大，如果是偶数把最小值flip两遍，如果是奇数把最小值flip一遍
        # 乘以2是因为之前加过，所以要减掉两次
        return sum(nums) - (k - i) % 2 * min(nums) * 2
