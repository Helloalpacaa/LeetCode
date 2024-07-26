class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(parent: int, child: int) -> Tuple[int, int]:
            maxDepth1, maxDepth2 = 0, 0

            for nextNode in graph[child]:
                if nextNode != parent:
                    depth = dfs(child, nextNode)[0]
                    if depth > maxDepth1:
                        maxDepth1, maxDepth2 = depth, maxDepth1
                    elif depth > maxDepth2:
                        maxDepth2 = depth
                    self.diameter = max(self.diameter, maxDepth1 + maxDepth2)
            
            return (maxDepth1 + 1, maxDepth2 + 1)
        
        self.diameter = 0
        dfs(-1, 0)
        return self.diameter
        