class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # 计算出prefix sum, 对于index为index % k的prefix sum持续维护一个最低值
        # nums = [-1, -2, -3, -4, -5, 8, 10, 31], k = 4
        # prefix_sum = [-1, -3, -6, -10, -15, -7, 3, 34]
        # 假设index为i = 7, nums[i] == 31时，要想求出subarray的最大值，就要用current prefix_sum - prefix_sum[3] or 0
        # 那么具体减哪一个呢，因为8, 4, 0在%k时有相同的余数0，所以我们只需要维护一个min_prefix_sum with size k取其中最小值

        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        min_prefix = [float('inf')] * k
        min_prefix[k-1] = 0 # 为的是当i == k - 1时，可以用prefix_sum[i] - 0来得到第一个ans
        ans = float('-inf')
        
        for i in range(n):
            ans = max(ans, prefix_sum[i] - min_prefix[i % k])
            min_prefix[i % k] = min(min_prefix[i % k], prefix_sum[i])
        
        return ans


