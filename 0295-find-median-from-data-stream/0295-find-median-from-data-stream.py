class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        
    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.minHeap, -heappushpop(self.maxHeap, -num))
        else:
            heappush(self.maxHeap, -heappushpop(self.minHeap, num))
        

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) /2
        else:
            return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()