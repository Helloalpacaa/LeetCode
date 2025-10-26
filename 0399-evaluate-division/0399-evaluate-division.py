class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        def dfs(curr, target, visited) -> float:
            if curr not in graph or target not in graph:
                return -1.0
            
            if curr == target:
                return 1.0
            
            visited.add(curr)
            for nxt, value in graph[curr].items():
                if nxt in visited:
                    continue
                res = dfs(nxt, target, visited)
                if res != -1.0:
                    return res * value
            
            return -1.0

        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        
        return res