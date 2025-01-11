class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        
        def bellman(pairs: List[List[str]], rates: List[float]) -> None:
            for _ in range(len(pairs)):
                for i in range(len(pairs)):
                    best[pairs[i][1]] = max(best[pairs[i][1]], best[pairs[i][0]] * rates[i])
                    best[pairs[i][0]] = max(best[pairs[i][0]], best[pairs[i][1]] / rates[i])
        
        best = defaultdict(int)
        best[initialCurrency] = 1
        bellman(pairs1, rates1)
        bellman(pairs2, rates2)

        return best[initialCurrency]
            