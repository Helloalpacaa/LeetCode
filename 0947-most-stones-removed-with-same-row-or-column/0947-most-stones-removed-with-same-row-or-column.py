class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(u):
            if u != parent.setdefault(u, u):
                parent[u] = find(parent[u])
            return parent[u]
        
        def join(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        # 把每个石头的row index和col index union在一起
        for u, v in stones:
            join(u, v + 100001)
        
        # 找出所有独立的root
        roots = set()
        for u, v in stones:
            roots.add(find(u))
        
        return len(stones) - len(roots)