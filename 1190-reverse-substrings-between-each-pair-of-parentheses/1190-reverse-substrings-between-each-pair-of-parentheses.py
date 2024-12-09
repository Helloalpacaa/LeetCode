class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']

        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                reversed_string = stack.pop()[::-1]
                stack[-1] += reversed_string
                # uevoli
            else:
                stack[-1] += char
        
        return stack[0]
            