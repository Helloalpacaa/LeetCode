class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        father = [i for i in range(n + 1)]

        def find(u) -> int:
            if u != father[u]:
                father[u] = find(father[u])
            return father[u]
        
        def join(u, v) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        res = []
        for u, v in edges:
            if find(u) != find(v):
                join(u, v)
            else:
                res = [u, v]
        
        return res