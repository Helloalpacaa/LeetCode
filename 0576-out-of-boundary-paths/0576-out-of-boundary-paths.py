class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        memo = {}

        def dfs(i: int, j: int, maxMove: int) -> int:
            if maxMove < 0:
                return 0

            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            key = i, j, maxMove
            if key in memo:
                return memo[key]

            memo[key] = (
                        dfs(i + 1, j, maxMove - 1) +
                        dfs(i - 1, j, maxMove - 1) + 
                        dfs(i, j + 1, maxMove - 1) + 
                        dfs(i, j - 1, maxMove - 1)
            )

            return memo[key]
        
        return dfs(startRow, startColumn, maxMove)