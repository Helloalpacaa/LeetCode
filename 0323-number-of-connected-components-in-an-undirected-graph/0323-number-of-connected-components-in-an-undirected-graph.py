class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(u) -> int:
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def join(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        components = n
        for u, v in edges:
            if find(u) != find(v):
                components -= 1
                join(u, v)
        
        return components