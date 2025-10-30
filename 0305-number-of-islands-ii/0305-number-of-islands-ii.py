class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        count = 0
        res = []

        def find(u):
            if u != parent.setdefault(u, u):
                parent[u] = find(parent[u])
            return parent[u]

        def join(u, v):
            nonlocal count
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
                count -= 1
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        lands = set()
        for i, j in positions:
            index = i * n + j
            if index in lands:
                res.append(count)
                continue
                
            lands.add(index)
            parent[index] = index
            count += 1

            for dr in directions:
                ni, nj = i + dr[0], j + dr[1]
                nid = ni * n + nj
                if 0 <= ni < m and 0 <= nj < n and nid in lands:
                    join(index, nid)
            
            res.append(count)
        
        return res
