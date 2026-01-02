class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)] # min_heap store (level, i, j)
        time = 0

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = {(0, 0)}

        while pq:
            level, i, j = heapq.heappop(pq)
            time = max(time, level)

            if i == n - 1 and j == n - 1:
                return time
            
            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    heapq.heappush(pq, (grid[ni][nj], ni, nj))
        


