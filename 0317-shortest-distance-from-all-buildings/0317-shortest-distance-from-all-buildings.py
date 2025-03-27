class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # distance[i][j] stores the distance from building (i, j) to all 0
        distance = [[0] * n for _ in range(m)]
        # reach[i][j]: number of buildings can reach from (i, j)
        reach = [[0] * n for _ in range(m)]
        buildings = sum(grid[i][j] == 1 for i in range(m) for j in range(n))

        # Use bfs to calculate the distance from building (i, j) to all the 0s it can reach
        def bfs(i: int, j: int) -> None:
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            queue = deque([(i , j, 0)])
            visited = set()

            while queue:
                x, y, dist = queue.popleft()
                for direction in directions:
                    nx, ny = x + direction[0], y + direction[1]

                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        reach[nx][ny] += 1
                        distance[nx][ny] += (dist + 1)
                        queue.append((nx, ny, dist + 1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        ans = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildings:
                    ans = min(ans, distance[i][j])
        
        return ans if ans != float('inf') else -1