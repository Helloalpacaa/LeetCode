class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = {}

        def find(u):
            if u not in parent:
                parent[u] = u
            if u != parent[u]:
                parent[u] = find(parent[u])
            return parent[u]

        def join(u, v):
            parent.setdefault(u, u)
            parent.setdefault(v, v)
            u = find(u)
            v = find(v)
            if u != v:
                parent[v] = u
        
        def prime_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors.add(d)
                    x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors
        
        # 1. 对每个数，把它和它所有的质数union
        for num in nums:
            factors = prime_factors(num)
            for f in factors:
                join(f, num)
        
        # 2. 统计每个连通分量中包含的数的数量
        count = defaultdict(int)
        max_size = 0
        for num in nums:
            root = find(num)
            count[root] += 1
            max_size = max(max_size, count[root])
        
        return max_size

        