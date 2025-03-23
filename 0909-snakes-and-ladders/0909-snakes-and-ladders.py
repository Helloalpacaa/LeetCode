class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_coordinates(points) -> (int, int):
            points -= 1
            row = n - 1 - points // n
            col = points % n if (n - 1 - row) % 2 == 0 else n - 1 - points % n

            return (row, col)
        
        queue = deque([1])
        visited = set([1])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                print(queue)
                points = queue.popleft()

                for i in range(1, 7):
                    next_points = points + i
                    if next_points <= n * n: 
                        row, col = get_coordinates(next_points)
                        
                        if board[row][col] != -1:
                            next_points = board[row][col]

                        if next_points == n * n:
                            return steps + 1

                        if next_points not in visited:
                            queue.append(next_points)
                            visited.add(next_points)
                
            steps += 1
        
        return -1
            


