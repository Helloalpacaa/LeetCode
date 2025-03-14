class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        nums.sort()

        while len(nums) >= 2 and nums[0] < k:
            num1 = heapq.heappop(nums)
            num2 = heapq.heappop(nums)
            new_num = num1 * 2 + num2
            heapq.heappush(nums, new_num)
            operations += 1
        
        return operations