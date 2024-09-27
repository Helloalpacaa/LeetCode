class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(ocean: List[List[int]], i: int, j: int) -> None:
            ocean[i][j] = True
            
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                
                if 0 <= next_i < m and 0 <= next_j < n and ocean[next_i][next_j] == False and heights[next_i][next_j] >= heights[i][j]:
                    dfs(ocean, next_i, next_j)
                    
        for row in range(m):
            dfs(pacific, row, 0)
            dfs(atlantic, row, n - 1)
        
        for col in range(n):
            dfs(pacific, 0, col)
            dfs(atlantic, m - 1, col)

        # print(pacific)

        ans = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        
        return ans
