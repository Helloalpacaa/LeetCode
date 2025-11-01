class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)] # (max_height so far, i , j)
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        visited = set()
        m, n = len(grid), len(grid[0])
        
        while min_heap:
            t, i, j = heapq.heappop(min_heap)
            if i == m - 1 and j == n - 1:
                return t

            if (i, j) in visited:
                continue
            
            visited.add((i, j))
                  
            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(min_heap, (max(t, grid[ni][nj]), ni, nj))
