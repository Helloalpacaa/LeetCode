class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        neighbor_sum = []
        for i in range(n - 1):
            neighbor_sum.append(weights[i] + weights[i + 1])

        neighbor_sum.sort()
        # print(neighbor_sum)

        max_score = sum(neighbor_sum[i] for i in range(n - k, n - 1))
        # print(n - k, n - 1)
        # print(max_score)
        min_score = sum(neighbor_sum[i] for i in range(k - 1))
        
        return max_score - min_score
