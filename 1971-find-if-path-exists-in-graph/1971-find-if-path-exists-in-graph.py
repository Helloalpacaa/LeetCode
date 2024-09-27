class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        father = [i for i in range(n)]

        def find(u: int) -> int:
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def union(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        for u, v in edges:
            union(u, v)
            if find(source) == find(destination):
                return True
        
        return False