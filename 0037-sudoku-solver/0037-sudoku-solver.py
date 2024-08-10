class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(row: int, col: int, val: str) -> bool:
            # check row
            for i in range(9):
                if board[row][i] == val or board[i][col] == val:
                    return False
            
            # check 3 * 3
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == val:
                        return False
            
            return True
        
        def backtracking() -> bool:
            for i in range(9):
                for j in range(9):
                    if board[i][j].isdigit():
                        continue
                    
                    for char in "123456789":
                        if isValid(i, j, char):
                            board[i][j] = char
                            if backtracking():
                                return True
                            board[i][j] = "."
                    return False
            
            return True
        
        backtracking()
                        
