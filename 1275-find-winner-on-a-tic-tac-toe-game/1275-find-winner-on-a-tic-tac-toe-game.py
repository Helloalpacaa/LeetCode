class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # 总共有8种方式结束游戏，三行row里有3个一样的player，三束column里有3个一样的player，两个对角线是一样的player
        # 用一个[0, 0, 0] 的list计算player在row 0, 1, 2 和column 0, 1, 2出现的数量
        # A + 1， B - 1，如果绝对值到达3了就说明某个player在这行出现了三次
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0
        player = 1

        for row, col in moves:
            rows[row] += player
            cols[col] += player

            if row == col:
                diag += player
            if row + col == 2:
                anti_diag += player
            
            if any(abs(line) == 3 for line in (rows[row], cols[col], diag, anti_diag)):
                return "A" if player == 1 else "B"
            
            player *= (-1)
        
        return "Draw" if len(moves) == 9 else "Pending"
