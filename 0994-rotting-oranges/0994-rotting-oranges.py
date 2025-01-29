class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotted = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotted.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while rotted and fresh > 0:
            size = len(rotted)
            while size:
                i, j = rotted.popleft()
                for direction in directions:
                    next_i = i + direction[0]
                    next_j = j + direction[1]
                    if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == 1:
                        grid[next_i][next_j] = 2
                        fresh -= 1
                        rotted.append((next_i, next_j))
                size -= 1
            minutes += 1
        
        return -1 if fresh > 0 else minutes


