class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = []
        for vector in vec:
            for num in vector:
                self.vec.append(num)
        self.pointer = 0

    def next(self) -> int:
        
        ans = self.vec[self.pointer]
        self.pointer += 1
        return ans

    def hasNext(self) -> bool:
        return self.pointer < (len(self.vec))


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()