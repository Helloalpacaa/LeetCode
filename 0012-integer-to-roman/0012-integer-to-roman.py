class Solution:
    def intToRoman(self, num: int) -> str:
        # 1. store the (value, simbol) tuple in a list, add value of 900, 400, 90, 40, 9, 4
        roman = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], 
                    [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]

        # 2. keep checking if num is greater than the value in the list, if it is, append the mathcing symbol into the answer
        ans = ""
        while num > 0:
            for value, symbol in roman:
                while num >= value:
                    ans += symbol
                    num -= value
        
        return ans