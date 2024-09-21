class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        # Check for a node with two parents
        child_parent = {}
        candidate1, candidate2 = None, None
        for u, v in edges:
            if v in child_parent:
                candidate1 = child_parent[v]
                candidate2 = [u, v]
                break
            child_parent[v] = [u, v]
        
        # If no node has two parents, find the edge that creates a cycle
        if not candidate1:
            for u, v in edges:
                if find(u) == find(v):
                    return [u, v]
                union(u, v)
        
        # If a node has two parents, check which edge can be removed
        else:
            for u, v in edges:
                if [u, v] == candidate2:
                    continue
                union(u, v)
            
            if find(candidate2[0]) == find(candidate2[1]):
                return candidate2
            return candidate1