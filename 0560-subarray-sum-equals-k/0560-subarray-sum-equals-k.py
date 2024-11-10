class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = dict()
        prefix_sum[0] = 1
        sum_ = 0

        for num in nums:
            sum_ += num
            count += prefix_sum.get(sum_ - k, 0)
            prefix_sum[sum_] = prefix_sum.get(sum_, 0) + 1
        
        
        return count