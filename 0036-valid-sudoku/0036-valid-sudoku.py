class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                
                # box_id from 0 - 8
                box_id = (i // 3) * 3 + j // 3

                if num in rows[i] or num in cols[j] or num in boxes[box_id]:
                    return False
                
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_id].add(num)
        
        return True