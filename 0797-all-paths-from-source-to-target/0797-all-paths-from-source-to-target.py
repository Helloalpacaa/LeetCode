class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        adj = defaultdict(list)
        for i, nodes in enumerate(graph):
            adj[i] = nodes
        
        res = []
        def dfs(node: int, path: list[int]) -> None:
            if node == n - 1:
                res.append(path.copy())
                return
            
            for nxt in adj[node]:
                path.append(nxt)
                dfs(nxt, path)
                path.pop()
        
        dfs(0, [0])
        return res
