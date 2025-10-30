class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
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
        
        def similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                if diff > 2:
                    return False
            
            return diff == 2 or diff == 0
        
        n = len(strs)
        for i in range(n - 1):
            for j in range(n):
                if similar(strs[i], strs[j]):
                    join(strs[i], strs[j])
        
        roots = set()
        for s in strs:
            root = find(s)
            roots.add(root)
        
        return len(roots)