class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efforts = [[float('inf')] * n for _ in range(m)]
        heap = [(0, 0, 0)] # (effort, x, y)
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        while heap:
            effort, x, y = heapq.heappop(heap)

            if x == m - 1 and y == n - 1:
                return effort

            for dr in directions:
                nx, ny = x + dr[0], y + dr[1]
                if 0 <= nx < m and 0 <= ny < n:
                    new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                    if new_effort < efforts[nx][ny]:
                        efforts[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))
        
        return -1
