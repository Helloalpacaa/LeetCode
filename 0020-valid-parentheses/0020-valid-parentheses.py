class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if char == ')' and stack and stack[-1] == "(":
                    stack.pop()
                elif char == ']' and stack and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0