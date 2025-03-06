class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operator = '+'
        num = 0

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp < 0 and num > 0:
                        tmp = -tmp
                        stack.append(-(tmp // num))
                    else:
                        stack.append(tmp // num)
                
                operator = s[i]
                num = 0
            
        return sum(stack)
                