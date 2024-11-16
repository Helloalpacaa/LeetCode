class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        father = [i for i in range(n)]

        def find(u: int) -> int:
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def join(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        for u, v in edges:
            if find(u) == find(v):
                return False
            join(u, v)
        
        return True