class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n:
            return -1
        
        parent = [i for i in range(n)]

        def find(u) -> int:
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def join(u, v) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        # Build components
        for u, v in connections:
            join(u, v)
        
        # Count unique roots (components)
        roots = set(find(i) for i in range(n))
        components = len(roots)

        return components - 1
        