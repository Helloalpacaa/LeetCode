class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memo = {}

        def backtracking(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_length = 1

            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]

                if 0 <= next_i < m and 0 <= next_j < n and matrix[next_i][next_j] > matrix[i][j]:
                    max_length = max(max_length, backtracking(next_i, next_j) + 1)
            
            memo[(i, j)] = max_length
            return max_length
        
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, backtracking(i, j))
        
        return longest_path
