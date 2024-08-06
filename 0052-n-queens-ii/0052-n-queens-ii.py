class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        board = [['.' for _ in range(n)] for _ in range(n)]

        def isValid(row: int, col: int) -> bool:
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1 , -1)):
                if board[i][j] == 'Q':
                    return False
            
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtracking(row: int) -> None:
            if row == n:
                self.ans += 1
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = 'Q'
                    backtracking(row + 1)
                    board[row][col] = '.'
        
        backtracking(0)
        return self.ans
