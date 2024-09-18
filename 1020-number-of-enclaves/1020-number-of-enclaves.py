class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # 从边界开始，遇到1就开始淹没1以及和它连接的1，最终再统计grid里1的数量
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            
            grid[i][j] = 0

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(m):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][n - 1] == 1:
                dfs(i, n - 1)
        
        for j in range(1, n - 1):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[m - 1][j] == 1:
                dfs(m - 1, j)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1

        return count

