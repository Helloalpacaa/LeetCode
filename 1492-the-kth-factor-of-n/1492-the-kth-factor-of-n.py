class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]

        for divider in range(n - 1, 0, -1):
            factor = n // divider
            if factor != factors[-1] and n % divider == 0:
                factors.append(factor)
        
        if k > len(factors):
            return -1
        else:
            return factors[k - 1]