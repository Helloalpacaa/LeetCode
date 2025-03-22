class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph.keys():
            graph[src].sort(reverse=True)
        
        print(graph)
        
        route = []

        def traverse(airport):
            while graph[airport]:
                traverse(graph[airport].pop())
            
            route.append(airport) # only add airports to the result once we’ve exhausted all paths from them
        
        traverse("JFK")
        return route[::-1]

