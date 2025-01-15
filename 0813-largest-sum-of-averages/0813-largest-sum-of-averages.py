class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        memo = {}

        def search(n, k) -> float:
            if (n, k) in memo:
                return memo[n, k]

            if n < k:
                return 0
            
            if k == 1:
                memo[n, k] = sum(nums[:n]) / float(n)
                return memo[n, k]
            
            curr, memo[n, k] = 0, 0
            for i in range(n - 1, -1, -1):
                curr += nums[i]
                memo[n, k] = max(memo[n, k], search(i, k - 1) + curr / float(n - i))
            
            return memo[n, k]
        
        return search(len(nums), k)
            