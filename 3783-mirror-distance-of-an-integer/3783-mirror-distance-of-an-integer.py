class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n

        reverse = 0
        while n > 0:
            digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10
        
        return abs(original - reverse)
