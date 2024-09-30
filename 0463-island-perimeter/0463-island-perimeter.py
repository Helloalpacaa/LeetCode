class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        area = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        area -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        area -= 2
        
        return area