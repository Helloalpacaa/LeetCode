class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        def backtracking(i, j, k) -> bool:
            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#' # change the value is faster then using a set to track the visited grid
            
            for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if backtracking(next_i, next_j, k + 1):
                    return True
            
            board[i][j] = tmp

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtracking(i, j, 0):
                        return True
        
        return False