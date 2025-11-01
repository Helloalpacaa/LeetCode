class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        # p1, p2 = 0, 0
        # while p1 < len(v1) or p2 < len(v2):
        #     if p1 < len(v1):
        #         self.queue.append(v1[p1])
        #         p1 += 1
        #     if p2 < len(v2):
        #         self.queue.append(v2[p2])
        #         p2 += 1
        if v1:
            self.queue.append((v1, 0))
        if v2:
            self.queue.append((v2, 0))

        # 优化的写法，适用于有k个Iterator的情况
        # for v in vectors:
        #     if v:
        #         self.queue.append((v, 0))


    def next(self) -> int:
        v, i = self.queue.popleft()
        res = v[i]
        if i + 1 < len(v):
            self.queue.append((v, i + 1))
        return res
        
    def hasNext(self) -> bool:
        return len(self.queue) > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())