class Solution:
    def reverse(self, x: int) -> int:
        # negative = x < 0
        # x = abs(x)

        # Converting an integer to string takes O(log x) time
        # String reversal using slice takes O(log x) time as we process each digit
        # Converting back to integer takes O(log x)
        # Space Complexity: O(log x), we need to store the string representation of the number
        # reversed_number = int(str(x)[::-1])

        # result = -reversed_number if negative else reversed_number

        # if result < -2**31 or result > 2**31 - 1:
        #     return 0
        
        # return result

        sign = 1
        if x < 0:
            sign = -1
        
        result = 0
        x = abs(x)
        while x > 0:
            digit = x % 10
            x = x // 10

            if result > (2**31 - 1) // 10 or result > 2**31 // 10:
                return 0

            result = result * 10 + digit

        return result * sign
        