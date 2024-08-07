class Solution {
    public void solveSudoku(char[][] board) {
        backtracking(board);
    }

    private boolean backtracking(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                char c = board[i][j];
                if (c != '.') {
                    continue;
                }
                for (char k = '1'; k <= '9'; k++) {
                    if (isValid(board, i, j, k)) {
                        board[i][j] = k;
                        if (backtracking(board)) {
                            return true;
                        }
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
        return true;
    }

    private boolean isValid(char[][] board, int i, int j, char k) {
        for (int col = 0; col < 9; col++) {
            if (board[i][col] == k) {
                return false;
            }
        }

        for (int row = 0; row < 9; row++) {
            if (board[row][j] == k) {
                return false;
            }
        }

        int startRow = i / 3 * 3;
        int startCol = j / 3 * 3;
        for (int row = startRow; row < startRow + 3; row++) {
            for (int col = startCol; col < startCol + 3; col++) {
                if (board[row][col] == k) {
                    return false;
                }
            }
        }

        return true;
    }
}