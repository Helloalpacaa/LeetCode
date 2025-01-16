class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # nums.sort()
        # operations = 0 if nums[0] == 0 else 1
        
        # for i in range(1, len(nums)):
        #     if nums[i] != 0 and nums[i] != nums[i - 1]:
        #         operations += 1
        
        # return operations

        seen = set()
        seen.add(0)
        operations = 0

        for num in nums:
            if num not in seen:
                operations += 1
                seen.add(num)
        
        return operations