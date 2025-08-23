class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                ch, count = stack.pop()
                stack.append((ch, count + 1))
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append((char, 1))
        
        ans = ""
        for char, count in stack:
            for i in range(count):
                ans += char
        
        return ans