class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        father = [i for i in range(n)]
        
        # union find
        def find(u: int) -> int:
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def join(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        provinces = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    provinces -= 1
                    join(i, j)
        
        return provinces
