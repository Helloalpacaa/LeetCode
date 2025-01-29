class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        count = {}
        count[0] = 1
        ans = 0

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            if prefix_sum[i + 1] - k in count:
                ans += count[prefix_sum[i + 1] - k]
            count[prefix_sum[i + 1]] = count.get(prefix_sum[i + 1], 0) + 1
        
        return ans