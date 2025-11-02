class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
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
        
        for u, v in edges:
            if find(u) != find(v):
                join(u, v)
            else:
                return False
        
        return True