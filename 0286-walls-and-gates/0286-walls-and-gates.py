class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        

        while queue:
            i, j = queue.popleft()
            for direction in directions:
                next_i = i + direction[0]
                next_j = j + direction[1]
                if 0 <= next_i < m and 0 <= next_j < n and rooms[next_i][next_j] > rooms[i][j] + 1:
                    rooms[next_i][next_j] = rooms[i][j] + 1
                    queue.append((next_i, next_j))
