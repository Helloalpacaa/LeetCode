class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # invalid有两种情况
        # 1. 一个node有两个roots，也就是一个node有两个indegrees，需要砍掉一条边，使得另外的还是能组成一个valid tree
        # 2. 形成了一个circle，需要砍掉形成circle的那条边（更后面出现的那条）
        n = len(edges)

        # check for a node with two parents
        indegree = [0] * (n + 1)
        for u, v in edges:
            indegree[v] += 1
        
        # add the nodes with two indegrees into candidates, if there are any there should be two
        # with the second one has a higher priority to be returned
        candidate1, candidate2 = None, None
        for u, v in edges:
            if indegree[v] == 2:
                candidate1 = candidate2
                candidate2 = u, v  
        # candidate1在edges中在candidate2的前面，如果要return也是return candidate2，所以我们等会会先check不用candidate2去组成graph的情况
        
        # union find的base code
        father = [i for i in range(n + 1)]
        
        def join(u: int, v: int) -> None:
            u = find(u)
            v = find(v)
            if u == v:
                return
            father[v] = u
        
        def find(u: int) -> int:
            if u == father[u]:
                return u
            father[u] = find(father[u])
            return father[u]
        
        # 如果有indegrees为2的nodes
        if candidate2:
            # check如果不用candidate 2来组成graph，是否还是一个valid的graph
            for u, v in edges:
                if (u, v) == candidate2:
                    continue
                join(u, v)
            
            # 如果没有用到candidate2那条edge，那条edge上的nodes却还存在在graph里（connected with other nodes)，说明这是一条多余的边
            if find(candidate2[0]) == find(candidate2[1]):
                return candidate2
            else:
                return candidate1
        else:
            for u, v in edges:
                if find(u) == find(v):
                    return (u, v)
                join(u, v)
