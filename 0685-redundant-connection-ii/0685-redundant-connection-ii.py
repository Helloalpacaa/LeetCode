class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        inDegrees = [0] * (n + 1)
        for u, v in edges:
            inDegrees[v] += 1
        
        candidate1, candidate2 = None, None
        for u, v in edges:
            if inDegrees[v] == 2:
                candidate2 = candidate1
                candidate1 = u, v
            # 如果有indegree为2的node，candidate1是后出现的edge，candidate2是先出现的edge
        
        father = [i for i in range(n + 1)]

        def join(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u != v:
                father[v] = u
        
        def find(u: int) -> None:
            if u != father[u]:
                father[u] = find(father[u])
            return father[u]
        
        print(candidate1, candidate2)

        # 当candidate1不为None时，再次循环edges，不把candidate1 join进来，看是否还能组成一个connected graph，如果可以，return candidate1
        if candidate1:
            for u, v in edges:
                if (u, v) == candidate1:
                    continue
                join(u, v)
                
            if find(candidate1[0]) == find(candidate1[1]):
                return candidate1
            else:
                return candidate2
        else:
            # 如果没有candidate1，说明有环，找到组成环的edge
            for u, v in edges:
                if find(u) == find(v):
                    return [u, v]
                join(u, v)
        


