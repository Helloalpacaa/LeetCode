class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1])])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        steps = 0
        maze[entrance[0]][entrance[1]] = '+'
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for dr in directions:
                    ni, nj = i + dr[0], j + dr[1]
                    if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == '.':
                        if ni == 0 or ni == m - 1 or nj == 0 or nj == n - 1:
                            return steps + 1
                        maze[ni][nj] = '+'
                        queue.append((ni, nj))
            steps += 1
        
        return -1
