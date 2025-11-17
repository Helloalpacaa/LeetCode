class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 把[1, ..., n]放在它正确的位置上(n - 1)
        for i in range(n):
            # use nums[i] != nums[nums[i] - 1] instead of nums[i] != i + 1 since there might be duplicated elements
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]: 
                # print(i, nums[i], nums[nums[i] - 1])
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                # print(i, nums)
                # This seems fine, but the problem is that nums[i] appears multiple times, and nums[i] changes as part of the swap!
                corrected_index = nums[i] - 1
                nums[i], nums[corrected_index] = nums[corrected_index], nums[i]
        
        # 再iterate array，第一个nums[i] != i + 1的就是answer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1