class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Union Find
        # n = len(isConnected)
        # father = [i for i in range(n)]

        # def join(u, v) -> None:
        #     u = find(u)
        #     v = find(v)
        #     father[v] = u

        # def find(u) -> int:
        #     if father[u] != u:
        #         father[u] = find(father[u])
        #     return father[u]

        # provinces = n
        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and find(i) != find(j):
        #             provinces -= 1
        #             join(i, j)
        
        # return provinces

        # DFS
        visited = set()
        n = len(isConnected)

        def dfs(city) -> None:
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
