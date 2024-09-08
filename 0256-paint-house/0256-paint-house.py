class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        # dp[i][0]: 第i个房子涂红色的cost
        # dp[i][1]: 第i个房子涂蓝色的cost
        # dp[i][2]: 第i个房子涂绿色的cost
        dp = [[0] * 3 for _ in range(n)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        
        print(dp)
        
        
        return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])