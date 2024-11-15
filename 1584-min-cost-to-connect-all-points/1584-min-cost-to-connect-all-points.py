class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = [] # use a min-heap to pop up the min manhattan distance
        heapq.heappush(min_heap, (0, 0)) # (0, 0) represents the manhattan distance and the index, st first it's 0
        visited = set() # record the points we have visited
        min_cost = 0

        while len(visited) < n:
            cost, point = heapq.heappop(min_heap)
            if point in visited:
                continue
            visited.add(point)
            min_cost += cost

            for next_point in range(n): # get the index of all the other unvisited points
                if next_point not in visited:
                    x1, y1 = points[point][0], points[point][1]
                    x2, y2 = points[next_point][0], points[next_point][1]
                    manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(min_heap, (manhattan_distance, next_point)) 
                    # we need to push a tuple with manhattan_distance at first, so that the heap is sorted by manhattan_distance
        
        return min_cost


