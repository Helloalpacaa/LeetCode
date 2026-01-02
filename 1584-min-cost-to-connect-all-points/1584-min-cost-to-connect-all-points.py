class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # n = len(points)
        # edges = []
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
        #         distance = abs(x1 - x2) + abs(y1 - y2)
        #         heapq.heappush(edges, (distance, i, j))
        
        # # print(edges)
        # parent = [i for i in range(n)]

        # def find(u):
        #     if u != parent[u]:
        #         parent[u] = find(parent[u])
        #     return parent[u]
        
        # def join(u, v):
        #     u = find(u)
        #     v = find(v)
        #     if u != v:
        #         parent[v] = u
        
        # cost = 0
        # visited = 0
        # while edges:
        #     dist, u, v = heapq.heappop(edges)
        #     if find(u) == find(v):
        #         continue
        #     visited += 1
        #     if visited == n:
        #         break
        #     join(u, v)
        #     cost += dist
            
        # return cost

        n = len(points)
        heap = [(0, 0)] # distance, node
        visited = set()
        visited_points = 0
        cost = 0

        while heap and visited_points < n:
            dist, point = heapq.heappop(heap)
            if point in visited:
                continue
            visited.add(point)
            visited_points += 1
            cost += dist

            for next_point in range(n):
                if next_point not in visited:
                    x1, y1, x2, y2 = points[point][0], points[point][1], points[next_point][0], points[next_point][1]
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (distance, next_point))
        
        return cost



