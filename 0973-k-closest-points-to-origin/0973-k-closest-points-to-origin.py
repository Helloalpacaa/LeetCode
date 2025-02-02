class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            distance = x ** 2 + y ** 2
            heapq.heappush(min_heap, (-distance, i))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        ans = []
        for distance, i in min_heap:
            ans.append(points[i])
        
        return ans