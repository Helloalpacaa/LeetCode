class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 从pacific ocean的边界出发，mark能到达的cor
        # 再从Atlantic ocean的边界出发，mark能到达的cor
        # 如果一个cor能同时被到达 那就放进ans

        m = len(heights)
        n = len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(ocean: List[List[bool]], i, j) -> None:
            ocean[i][j] = True
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if 0 <= next_i < m and 0 <= next_j < n and heights[next_i][next_j] >= heights[i][j] and not ocean[next_i][next_j]:
                    dfs(ocean, next_i, next_j)

        for i in range(m):
            dfs(pacific, i, 0)
            dfs(atlantic, i, n - 1)
        for j in range(n):
            dfs(pacific, 0, j)
            dfs(atlantic, m - 1, j)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        
        return ans
        



        



        