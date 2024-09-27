class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        father = [i for i in range(n + 1)]

        def find(u: int) -> int:
            if u != father[u]:
                father[u] = find(father[u])
            return father[u]
        
        def union(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        ans = []
        for u, v in edges:
            if find(u) == find(v):
                ans = [u, v]
            union(u, v)
        
        return ans