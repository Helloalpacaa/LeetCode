class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 建立graph - adjacent list:[[(1, 100)], [(2, 100), (3, 600)], [(0, 100), (3, 200)], []]
        graph = [[] for _ in range(n)]
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        distance = [float('inf')] * n
        distance[src] = 0
        queue = deque([(src, 0, -1)]) # queue里存储node，price，stops

        while queue:
            size = len(queue)

            # Create a temp array to store the best prices at this level
            temp = distance.copy()

            while size:
                node, price, stops = queue.popleft()

                # # Skip if we've seen this state before
                # if (node, stops) in visited:
                #     size -= 1
                #     continue
                # visited.add((node, stops))

                # distance[node] = min(distance[node], price)
                
                for neighbor, cost in graph[node]:
                    if stops + 1 <= k and cost + price < distance[neighbor]:
                        queue.append((neighbor, cost + price, stops + 1))
                        temp[neighbor] = price + cost
                
                size -= 1
            
            distance = temp
        
        return -1 if distance[dst] == float('inf') else distance[dst]

        # graph = {city: [] for city in range(n)}
        # for source, destination, cost in flights: 
        #     graph[source].append((cost, destination))
        
        # heap = [(0, 0, src)]
        # visited = set()
        # heapq.heapify(heap)
        # cost_map = {city: float("inf") for city in range(n)}
        # cost_map[src] = 0
        # while heap: 
        #     stops, cost, city = heapq.heappop(heap)
        #     if (city, stops) in visited: 
        #         continue
        #     visited.add((city, stops))
        #     if stops > k: 
        #         continue
        #     for next_cost, neighbor in graph[city]: 
        #         if cost_map[neighbor] > cost + next_cost: 
        #             heapq.heappush(heap, (stops+1, cost+next_cost, neighbor))
        #             cost_map[neighbor] = cost + next_cost
        # if cost_map[dst] == float("inf"): 
        #     cost_map[dst] = -1
        # return cost_map[dst]