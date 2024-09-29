class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        queue = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        minutes = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh > 0 and queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                for direction in directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                        queue.append((next_i, next_j))
                        grid[next_i][next_j] = 2
                        fresh -= 1
            minutes += 1
        
        return -1 if fresh > 0 else minutes
