class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["." for _ in range(n)] for _ in range(n)]
    
        def isValid(row: int, col: int) -> bool:
            # check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # check upper-left diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            
            # check upper-right diagonal
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[i][j] == 'Q':
                    return False
            
            return True
        
        def backtracking(row: int) -> None:
            if row == n:
                ans.append([''.join(row) for row in board])
                return
            
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = 'Q'
                    backtracking(row + 1)
                    board[row][col] = '.'
        
        backtracking(0)
        return ans
        

            