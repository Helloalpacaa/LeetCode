class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if(backtracking(board, i, j, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean backtracking(char[][] board, int i, int j, String word, int index) {
        if (index == word.length()) {
            return true;
        }

        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(index)) {
            return false;
        }

        char tmp = board[i][j];
        board[i][j] = '#'; // 为了不让接下来的查找走回头路
        boolean ret = backtracking(board, i + 1, j, word, index + 1)
                    || backtracking(board, i - 1, j, word, index + 1)
                    || backtracking(board, i, j + 1, word, index + 1)
                    || backtracking(board, i, j - 1, word, index + 1);
        board[i][j] = tmp;
        return ret;
    }
}