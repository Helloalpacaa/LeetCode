class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        factor = 2

        # for divider in range(n - 1, 0, -1):
        #     factor = n // divider
        #     if factor != factors[-1] and n % divider == 0:
        #         factors.append(factor)

        while factors[-1] < n and len(factors) < k:
            if n % factor == 0:
                factors.append(factor)
            factor += 1
        
        if k > len(factors):
            return -1
        else:
            return factors[k - 1]