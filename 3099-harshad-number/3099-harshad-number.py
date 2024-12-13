class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits_sum = 0
        number = x

        while number > 0:
            digit = number % 10
            digits_sum += digit
            number = number // 10
        
        return digits_sum if x % digits_sum == 0 else -1