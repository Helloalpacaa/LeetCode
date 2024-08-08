class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []

        def isValid(row: int, col: int) -> bool:
            # check row
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            # check left upper
            for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False
            
            # check right upper
            for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[i][j] == "Q":
                    return False
            
            return True
        
        def backtracking(row: int) -> None:
            if row == n:
                ans.append(["".join(row) for row in board])
                return
            
            for i in range(n):
                if isValid(row, i):
                    board[row][i] = "Q"
                    backtracking(row + 1)
                    board[row][i] = "."
        
        backtracking(0)
        return ans