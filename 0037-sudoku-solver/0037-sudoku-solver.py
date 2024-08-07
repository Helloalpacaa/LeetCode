class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row: int, col: int, val: chr) -> bool:
            # check row
            for i in range(9):
                if board[row][i] == val:
                    return False
            
            # check col
            for j in range(9):
                if board[j][col] == val:
                    return False
            
            # check 3 * 3 subgrid
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == val:
                        return False
            
            return True
        
        def backtracking() -> bool:
            for i in range(9):
                for j in range(9):
                    # 如果是数字，去下一个格子
                    if board[i][j] != '.':
                        continue

                    # 如果是‘.'，看哪个数字可以放在这里
                    for val in "123456789":
                        if isValid(i, j, val):
                            board[i][j] = val
                            # 找到可以放在这里的数字后，继续当前棋盘
                            # 如果下一个格子“123456789”都不valid，会return False，那么当前格子的值会直接回溯，去测试下一个数字是否valid
                            # 如果找到一组合适立刻返回
                            if backtracking():
                                return True
                            board[i][j] = '.'
                    
                    # 如果试了9个数字都不valid，说明这个格子没有valid的值，return False结束
                    return False
            
            # 如果不曾return False，就return True
            return True
        
        backtracking()
