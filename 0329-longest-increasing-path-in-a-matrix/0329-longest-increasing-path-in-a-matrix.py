class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {}

        def dfs(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            longest_path = 1

            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]

                if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] > matrix[i][j]:
                    longest_path = max(longest_path, 1 + dfs(next_i, next_j))
            
            memo[(i, j)] = longest_path
            return longest_path
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        
        return ans