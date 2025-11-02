class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_coordinates(points) -> (int, int):
            points -= 1
            row = n - 1 - points // n
            col = points % n if (n - 1 - row) % 2 == 0 else n - 1 - points % n

            return (row, col)
        
        queue = deque([(1, 0)])
        visited = set([1])

        while queue:
            points, steps = queue.popleft()

            for i in range(1, 7):
                next_points = points + i
                row, col = get_coordinates(next_points)

                if board[row][col] != -1:
                    next_points = board[row][col]

                if next_points == n * n:
                    return steps + 1
                
                if next_points > n * n:
                    break

                if next_points not in visited:
                    queue.append([next_points, steps + 1])
                    visited.add(next_points)
        
        return -1
            


