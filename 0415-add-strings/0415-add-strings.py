class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        digits = []
        
        base = 1
        while i >= 0 or j >= 0 or carry > 0:
            number1 = int(num1[i]) if i >= 0 else 0
            number2 = int(num2[j]) if j >= 0 else 0

            total = number1 + number2 + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            
            digits.append(chr(total % 10 + 48))
            base *= 10
            i -= 1
            j -= 1
        
        return "".join(reversed(digits))


