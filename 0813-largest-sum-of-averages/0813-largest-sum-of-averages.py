class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # memo = {}

        # def search(n, k) -> float:
        #     if (n, k) in memo:
        #         return memo[n, k]

        #     if n < k:
        #         return 0
            
        #     if k == 1:
        #         memo[n, k] = sum(nums[:n]) / float(n)
        #         return memo[n, k]
            
        #     curr, memo[n, k] = 0, 0
        #     for i in range(n - 1, -1, -1):
        #         curr += nums[i]
        #         memo[n, k] = max(memo[n, k], search(i, k - 1) + curr / float(n - i))
            
        #     return memo[n, k]
        
        # return search(len(nums), k)

        N = len(nums)
        K = k
        # Calculate prefix sums for efficient range sum queries
        P = [0] * (N + 1)
        for i in range(N):
            P[i + 1] = P[i] + nums[i]
        
        # Initialize dp array
        # dp[i][k] represents the maximum score for first i numbers divided into k groups
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        
        # Base case: k=1, calculating average for each prefix
        for i in range(1, N + 1):
            dp[i][1] = P[i] / i
        
        # Fill dp table
        for k in range(2, K + 1):
            for i in range(k, N + 1):
                for j in range(k - 1, i):
                    # dp[j][k-1] represents score for first j elements in k-1 groups
                    # (P[i] - P[j]) / (i - j) represents average of elements from j to i
                    dp[i][k] = max(dp[i][k], 
                                dp[j][k-1] + (P[i] - P[j]) / (i - j))
        
        return dp[N][K]
                