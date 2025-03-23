class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(pos: int) -> (int, int):
            pos -= 1

            row = n - 1 - pos // n
            col = pos % n if (n - 1 - row) % 2 == 0 else n - 1 - pos % n

            return (row, col)
        
        queue = deque([(1, 0)]) # pos, moves
        visited = set([1])

        while queue:
            pos, moves = queue.popleft()

            for i in range(1, 7):
                next_pos = pos + i

                row, col = get_coordinates(next_pos)

                if board[row][col] != -1:
                    next_pos = board[row][col]
                
                if next_pos == n * n:
                    return moves + 1
                
                if next_pos > n * n:
                    break
                
                if next_pos not in visited:
                    queue.append((next_pos, moves + 1))
                    visited.add(next_pos)

        return -1
