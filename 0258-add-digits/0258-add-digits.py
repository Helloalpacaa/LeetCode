class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num = num // 10
            
            if total >= 10:
                num = total
            else:
                return total
        
        return num
        