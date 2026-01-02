class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = [(0, points[0][0], points[0][1])]
        cost = 0
        unvisited = set((x, y) for x, y in points)

        while pq:
            dist, x, y = heapq.heappop(pq)
            if (x, y) not in unvisited:
                continue

            cost += dist
            unvisited.remove((x, y))

            if not unvisited:
                return cost

            for next_point in unvisited:
                next_x, next_y = next_point[0], next_point[1]
                val = abs(x - next_x) + abs(y - next_y)
                heapq.heappush(pq, (val, next_x, next_y))


