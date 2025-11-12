class SnakeGame:

    dr = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = food
        self.food_index = 0
        self.n = width
        self.m = height
        self.snake_body = deque([(0, 0)])
        self.snake_set = {(0, 0)}
        self.score = 0


    def move(self, direction: str) -> int:
        directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        dr, dc = directions[direction]
        nr, nc = self.snake_body[0][0] + dr, self.snake_body[0][1] + dc

        tail = self.snake_body[-1]
        self.snake_set.remove(tail)

        if nr < 0 or nr >= self.m or nc < 0 or nc >= self.n or ((nr, nc) in self.snake_set):
            return -1
        
        self.snake_body.appendleft((nr, nc))
        self.snake_set.add((nr, nc))

        if self.food_index < len(self.food) and [nr, nc] == self.food[self.food_index]:
            self.score += 1
            self.food_index += 1
            self.snake_set.add(tail)
        else:
            self.snake_body.pop()
        
        return self.score
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)