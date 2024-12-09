class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(s)}  # Fix: Switched `char` and `idx`
        stack = []
        visited = set()

        for i in range(len(s)):
            char = s[i]

            if char in visited:
                continue
            
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                visited.remove(removed)
            
            stack.append(char)
            visited.add(char)
        
        return "".join(stack)