class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 这种解法逻辑上是对的，但是超时，因为我们重复计算了很多次相同格子的值
        # if maxMove < 0:
        #     return 0
        
        # # 如果当前position不在boundry内，说明找到了一条valid path，return 1
        # if not (0 <= startRow < m and 0 <= startColumn < n):
        #     return 1

        # return (self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) + 
        #         self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1) + 
        #         self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) + 
        #         self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)) % 1000000007
        
        # 用一个Dict存储我们所有计算过的值，用当前row, 当前column, 剩余maxMove组成key
        MOD = 10**9 + 7
        memo = {}

        def dfs(i: int, j: int, maxMove: int) -> int:
            if maxMove <0 :
                return 0
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            key = i, j, maxMove
            if key in memo:
                return memo[key]
            
            memo[key] = (
                dfs(i, j - 1, maxMove - 1) + 
                dfs(i, j + 1, maxMove - 1) + 
                dfs(i - 1, j, maxMove - 1) +
                dfs(i + 1, j, maxMove - 1)
            )

            return memo[key] % MOD
        
        return dfs(startRow, startColumn, maxMove)