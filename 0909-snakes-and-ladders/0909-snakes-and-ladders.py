class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def num_to_index(points: int) -> (int, int):
            # i = 5, j = 0 -> 1, m = n = sqrt(36) = 6
            points -= 1
            row = n - 1 - points // n
            col = points % n if( n - 1 - row) % 2 == 0 else n - 1 - points % n

            return row, col
        
        queue = deque([1])
        visited = {1}
        steps = 0

        while queue:
            for _ in range(len(queue)):
                points = queue.popleft()

                if points == n * n:
                    return steps
                
                # print(points)

                for nxt in range(points + 1, min(points + 6, n * n) + 1):
                    ni, nj = num_to_index(nxt)
                    val = board[ni][nj] if board[ni][nj] != -1 else nxt

                    if val not in visited:
                        queue.append(val)
                        visited.add(val)
            
            steps += 1

        return -1




