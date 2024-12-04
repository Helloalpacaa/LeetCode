class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # # 1. define a list with each element has its own as their father
        # n = len(isConnected)
        # father = [i for i in range(n)]

        # # union find
        # # join two proinces if they don't have the same father
        # def join(u, v) -> None:
        #     u = find(u)
        #     v = find(v)
        #     if u != v:
        #         father[v] = u
        
        # # find and return the father of u, also using path compress
        # def find(u) -> int:
        #     if u != father[u]:
        #         father[u] = find(father[u])
        #     return father[u]
        
        # # iterate each element in isConnected, if isConencted[i][j] == 1, 
        # # and i and j don't have the same parent, join them and decrement provinces
        # provinces = n
        # for i in range(n):
        #     for j in range(n):
        #         if i != j and isConnected[i][j] == 1:
        #             if find(i) != find(j):
        #                 join(i, j)
        #                 provinces -= 1
        
        # return provinces

        # dfs
        visited = set()
        n = len(isConnected)

        def dfs(city):
            visited.add(city)

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)
        
        provinces = 0
        for city in range(n):
            if city not in visited:
                provinces += 1
                dfs(city)
        
        return provinces
        