class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # maintain a min-heap storing (diff, row, col)
        m, n = len(heights), len(heights[0])
        pq = [(0, 0, 0)]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        visited = [[False] * n for _ in range(m)]
        maxdiff = float("-inf")

        while pq:
            diff, i, j = heapq.heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = True
            maxdiff = max(maxdiff, diff)

            if i == m - 1 and j == n - 1:
                return maxdiff
            
            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    heapq.heappush(pq, (abs(heights[i][j] - heights[ni][nj]), ni, nj))
        

