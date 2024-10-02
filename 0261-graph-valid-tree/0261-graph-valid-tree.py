class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        father = [i for i in range(n)]

        def join(u, v) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        def find(u) -> int:
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        if len(edges) < n - 1:
            return False
        
        for u, v in edges:
            if find(u) == find(v):
                return False
            join(u, v)
        
        return True