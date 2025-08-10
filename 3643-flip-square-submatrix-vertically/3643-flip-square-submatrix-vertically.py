class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        up, bottom = x, x + k

        while up < bottom:
            for i in range(y, y + k):
                grid[up][i], grid[bottom - 1][i] = grid[bottom - 1][i], grid[up][i]
            
            up += 1
            bottom -= 1
        
        return grid

        