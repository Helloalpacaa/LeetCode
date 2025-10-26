class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(i: int, j: int, word_index: int, visited) -> bool:
            if word_index == len(word) - 1:
                return True
            
            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and board[ni][nj] == word[word_index + 1]:
                    visited.add((ni, nj))
                    if dfs(ni, nj, word_index + 1, visited):
                        return True
                    visited.remove((ni, nj))

            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, {(i, j)}):
                        return True
        
        return False

            
            