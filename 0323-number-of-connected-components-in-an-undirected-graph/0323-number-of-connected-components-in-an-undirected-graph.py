class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
        
        count = n
        for u, v in edges:
            if find(u) != find(v):
                count -= 1
                join(u, v)
        
        return count