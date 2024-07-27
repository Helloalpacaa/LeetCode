class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        self.diameter = 0

        def traversal(parent: int, child: int) -> int:
            maxDepth1, maxDepth2 = 0, 0

            for grandchild in self.graph[child]:
                if grandchild != parent:
                    depth = traversal(child, grandchild)
                    if depth > maxDepth1:
                        maxDepth1, maxDepth2 = depth, maxDepth1
                    elif depth > maxDepth2:
                        maxDepth2 = depth

            self.diameter = max(self.diameter, maxDepth1 + maxDepth2)
            
            return maxDepth1 + 1
        
        traversal(-1, 0)
        return self.diameter
        
