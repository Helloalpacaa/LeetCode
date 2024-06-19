class MedianFinder:

    def __init__(self):
        self.largerHalf = []
        self.smallerHalf = []
        
    def addNum(self, num: int) -> None:
        if len(self.largerHalf) == len(self.smallerHalf):
            heapq.heappush(self.largerHalf, -heapq.heappushpop(self.smallerHalf, -num))
        else:
            heapq.heappush(self.smallerHalf, -heapq.heappushpop(self.largerHalf, num))
        
    def findMedian(self) -> float:
        if len(self.largerHalf) == len(self.smallerHalf):
            return (self.largerHalf[0] - self.smallerHalf[0]) / 2
        else:
            return self.largerHalf[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()