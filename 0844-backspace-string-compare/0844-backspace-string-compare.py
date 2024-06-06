class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            
            return stack
        
        peocessedS = processString(s)
        peocessedT = processString(t)
        
        return peocessedS == peocessedT