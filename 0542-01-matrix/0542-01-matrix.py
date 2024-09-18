class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[float('inf')] * n for _ in range(m)]
        queue = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append([i, j])
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set([])

        while queue:
            i, j = queue.popleft()
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                key = next_i, next_j
                if next_i >= 0 and next_i < m and next_j >= 0 and next_j < n and key not in visited:
                    ans[next_i][next_j] = min(ans[next_i][next_j], ans[i][j] + 1)
                    queue.append([next_i, next_j])
            visited.add((i, j))

        return ans
