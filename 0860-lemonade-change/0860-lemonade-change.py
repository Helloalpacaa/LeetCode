class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            else:
                if ten > 0:
                    ten -= 1
                else:
                    five -= 2
                five -= 1
                twenty += 1
            
            if five < 0 or ten < 0:
                return False
        
        return True