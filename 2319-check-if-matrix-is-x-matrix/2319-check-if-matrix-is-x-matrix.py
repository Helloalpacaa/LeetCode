class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        start = 0
        end = n - 1

        while start < end:
            if grid[start][start] == 0 or grid[start][end] == 0 or grid[end][start] == 0 or grid[end][end] == 0:
                return False
            for idx in range(start + 1, end):
                if grid[start][idx] != 0 or grid[end][idx] != 0 or grid[idx][start] != 0 or grid[idx][end] != 0:
                    return False
            
            start += 1
            end -= 1
        
        return True
