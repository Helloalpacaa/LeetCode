class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        corners = [(0, 0), (0, n - 1), (m - 1, 0), (m - 1, n - 1)]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i: int, j: int):
            res = [i, j]
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] > mat[i][j]:
                    res = dfs(ni, nj)
            
            return res
        
        corners.sort(reverse=True)
        for corner in corners:
            return dfs(corner[0], corner[1])