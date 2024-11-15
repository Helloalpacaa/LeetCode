class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Use a stack and set to collect the indices need to be removed
        # Then iterate the string again to remove these indices

        stack = []
        remove = set()

        for i in range(len(s)):
            char = s[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        remove.update(stack)

        ans = ""
        for i in range(len(s)):
            if i not in remove:
                ans += s[i]
        
        return ans