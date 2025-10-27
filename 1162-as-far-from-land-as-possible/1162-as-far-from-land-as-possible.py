class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
        
        max_distance = -1
        while queue:
            i, j, distance = queue.popleft()
            
            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    max_distance = max(max_distance, distance + 1)
                    queue.append((ni, nj, distance + 1))
        
        return max_distance


        
        