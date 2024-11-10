class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def getArea(i, j) -> int:
            # Check if the coordinate is out of boundry or is water
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            # Mark the island as visited
            grid[i][j] = 0

            return 1 + getArea(i + 1, j) + getArea(i - 1, j) + getArea(i, j + 1) + getArea(i, j - 1)
        
        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, getArea(i, j))
        
        return maxArea
