class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7
        dp = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, last) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] <= last:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            curr = grid[i][j]
            dp[i][j] = (1 + dfs(i - 1, j, curr) + dfs(i + 1, j, curr) + dfs(i, j - 1, curr) + dfs(i, j + 1, curr)) % mod
            return dp[i][j]
        
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         count += dfs(i, j, 0)
        
        # return count
        return sum(dfs(i, j, -1) for i in range(m) for j in range(n)) % mod

        