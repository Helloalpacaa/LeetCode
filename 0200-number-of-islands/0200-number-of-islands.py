class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # flood the adjacent islands
        def dfs(i, j) -> None:
            # check edge
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            # flood the island by changing its value to '0'
            grid[i][j] = '0'

            # flood its adjencent islands recursively
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # Iterating the grid, if we see an island, flood its adjencent lands
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count