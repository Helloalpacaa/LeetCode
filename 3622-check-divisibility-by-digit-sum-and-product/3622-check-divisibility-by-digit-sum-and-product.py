class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total = 0
        product = 1

        for digit in str(n):
            total += int(digit)
            product *= int(digit)
        
        print(total)
        print(product)
        
        return n % (total + product) == 0