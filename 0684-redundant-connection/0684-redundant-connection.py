class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        father = [i for i in range(n + 1)]

        def find(u: int) -> int:
            if u == father[u]:
                return u
            father[u] = find(father[u])
            return father[u]

        def join(u, v) -> None:
            u = find(u)
            v = find(v)
            if u == v:
                return
            father[v] = u
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            if find(u) == find(v):
                ans = edge
            join(u, v)
            
        return ans