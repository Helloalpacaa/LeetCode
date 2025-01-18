class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 建立graph - adjacent list:[[(1, 100)], [(2, 100), (3, 600)], [(0, 100), (3, 200)], []]
        graph = [[] for _ in range(n)]
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        print(graph)
        stops = 0
        cheapest_price = float('inf')
        queue = deque([(src, 0, -1)]) # queue里存储node，price，stops
        distance = [float('inf')] * n
        distance[src] = 0

        while queue:
            size = len(queue)
            while size:
                node, price, stops = queue.popleft()
                distance[node] = min(distance[node], price)
                
                for neighbor, cost in graph[node]:
                    if stops + 1 <= k and cost + price < distance[neighbor]:
                        queue.append((neighbor, cost + price, stops + 1))
                
                size -= 1
        
        return -1 if distance[dst] == float('inf') else distance[dst]
