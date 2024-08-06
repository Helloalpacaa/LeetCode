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
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # check upper-right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
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
        

            