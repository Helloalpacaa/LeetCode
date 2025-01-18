class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif (
                    stack[-1] == '(' and char == ')' or
                    stack[-1] == '{' and char == '}' or 
                    stack[-1] == '[' and char == ']'
                    ):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0