class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, x2, y2 = points[i][0], points[i][1], points[j][0], points[j][1]
                distance = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(edges, (distance, i, j))
        
        # print(edges)
        parent = [i for i in range(n)]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def join(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        cost = 0
        while edges:
            dist, u, v = heapq.heappop(edges)
            if find(u) == find(v):
                continue
            
            join(u, v)
            cost += dist
            
        return cost

