class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append([i, j])

        minute = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while fresh > 0 and queue:
            size = len(queue)
            while size > 0:
                i, j = queue.popleft()
                for direction in directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                        fresh -= 1
                        queue.append([next_i, next_j])
                        grid[next_i][next_j] = 2
                size -= 1
            minute += 1
        
        return minute if fresh == 0 else -1

