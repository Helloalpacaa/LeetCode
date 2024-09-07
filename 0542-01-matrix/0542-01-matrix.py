class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        # memo = {}
        
        # def dfs(i: int, j: int) -> int:
        #     if i < 0 or i >= m or j < 0 or j >= n:
        #         return float('inf')
            
        #     if mat[i][j] == 0:
        #         return 0
            
        #     key = i, j
        #     if key in memo:
        #         return memo[key]

        #     memo[key] = float('inf')

        #     memo[key] = 1 + min(dfs(i, j - 1), dfs(i, j + 1), dfs(i - 1, j), dfs(i + 1, j))

        #     return memo[key]
        
        # ans = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         ans[i][j] = dfs(i, j)
        
        # return ans
        
        #这题不适合用DFS做，哪怕用一个Dict存储所有visit过的cell，最坏的情况它可能还需要不断revisit这些计算过的cell
        #这种求最短路程的题，考虑用BFS，直接从值为0的cell出发向外扩展，就保证了它是最小路径
        ans = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while queue:
            x, y = queue.popleft()
            for direction in directions:
                nx, ny = x + direction[0], y + direction[1]
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] > ans[x][y] + 1:
                    ans[nx][ny] = ans[x][y] + 1
                    queue.append((nx, ny))
        
        return ans

