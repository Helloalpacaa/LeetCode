class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 从边缘的“O”出发，把所有和它连在一起的“O"改成一个特殊的"*"
        # 再遍历一遍board，把"*"改回"O"，把其余的"O"改成"X"

        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == 'X':
                return
            
            board[i][j] = '*'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][n - 1] == 'O':
                dfs(row, n - 1)
        
        for col in range(1, n - 1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[m - 1][col] == 'O':
                dfs(m - 1, col)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '*':
                    board[i][j] = 'O'