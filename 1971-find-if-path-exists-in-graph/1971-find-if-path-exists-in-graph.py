class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        father = [i for i in range(n)]
        
        def find(u: int) -> int:
            if u == father[u]:
                return u
            else:
                father[u] = find(father[u])
                return father[u]

        
        def join(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u == v:
                return
            father[v] = u

        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            join(u, v)
        
        print(father)
        
        return find(source) == find(destination)


        


