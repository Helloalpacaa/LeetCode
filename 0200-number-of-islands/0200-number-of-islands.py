class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        def submerge(i: int, j: int) -> None:
            grid[i][j] = "0"

            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                    submerge(ni, nj)
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    submerge(i, j)
        
        return islands

