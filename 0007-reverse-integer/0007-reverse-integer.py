class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        if x < 0:
            x = -x
        
        res = 0
        while x > 0:
            digit = x % 10
            res = res * 10 + digit

            if res >= 2**31 - 1:
                return 0

            x //= 10
        
        return res * sign
