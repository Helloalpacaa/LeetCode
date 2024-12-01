class Solution:
    def addDigits(self, num: int) -> int:
        # 349
        # 3 + 4 + 9 = 16
        # 1 + 6 = 7
        

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
        