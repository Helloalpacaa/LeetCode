class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack = []

        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                if stack and stack[-1].isdigit():
                    stack[-1] = str(int(stack[-1]) * 10 + int(c))
                else:
                    stack.append(c)
            elif c == '[':
                stack.append("")
            elif c == ']':
                word = stack.pop()
                repeat = int(stack.pop())
                new_word = ""
                for _ in range(repeat):
                    new_word += word
                if stack:
                    stack[-1] += new_word
                else:
                    res += new_word
            else:
                if stack:
                    stack[-1] += c
                else:
                    res += c
                # print(i, c, stack)
                
            
            i += 1
        
        return res
                
            