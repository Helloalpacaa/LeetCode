class Solution:
    def reverse(self, x: int) -> int:
        # store the sign of x
        sign = 1
        if x < 0:
            sign = -1
        x = abs(x)
        
        ans = 0
        while x > 0:
            digit = x % 10
            x = x // 10

            if ans  > (2**31 - 1) // 10:
                return 0

            ans = ans * 10 + digit
        
        return ans * sign
        
