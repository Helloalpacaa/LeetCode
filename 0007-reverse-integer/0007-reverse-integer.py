class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        
        x = abs(x)
        reversed_number = int(str(x)[::-1])

        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0
        
        return reversed_number * sign