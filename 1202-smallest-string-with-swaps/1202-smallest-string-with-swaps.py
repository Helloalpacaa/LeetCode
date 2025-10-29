class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = [i for i in range(n)]

        def find(u):
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]
        
        def join(u, v):
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        for u, v in pairs:
            join(u, v)
        
        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)
        
        res = list(s)
        for indices in groups.values():
            indices.sort()
            chars = sorted(res[i] for i in indices)
            for idx, ch in zip(indices, chars):
                res[idx] = ch
        
        return "".join(res)