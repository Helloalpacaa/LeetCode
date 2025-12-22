class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        total = 0
        costs = defaultdict(int)

        for i in range(len(s)):
            costs[s[i]] += cost[i]
            total += cost[i]
        
        max_cost = max(costs.values())
        return total - max_cost