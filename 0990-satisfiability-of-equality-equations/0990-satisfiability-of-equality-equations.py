class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
        
        for equation in equations:
            a, b = equation[0], equation[3]
            if equation[1:3] == "==":
                join(a, b)
        
        for equation in equations:
            a, b = equation[0], equation[3]
            if equation[1:3] == "!=":
                if find(a) == find(b):
                    return False
        
        return True