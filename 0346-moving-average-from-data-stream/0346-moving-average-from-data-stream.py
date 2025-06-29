class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.moving_array = deque()

    def next(self, val: int) -> float:
        if len(self.moving_array) >= self.size:
            self.moving_array.popleft()
        self.moving_array.append(val)
        return sum(self.moving_array) / len(self.moving_array)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)