class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(i: int, j: int, word_index: int) -> bool:
            if word_index == len(word) - 1:
                return True
            
            tmp = board[i][j]
            board[i][j] = '.'

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[word_index + 1]:
                    if dfs(ni, nj, word_index + 1):
                        return True
            
            board[i][j] = tmp
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False

