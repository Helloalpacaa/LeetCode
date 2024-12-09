class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Step 1: Track the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        stack = []
        visited = set()

        # Step 2: Iterate through the string
        for idx, char in enumerate(s):
            # Skip if the character is already in the result
            if char in visited:
                continue

            # Maintain lexicographical order by removing characters
            # that are larger than the current one and appear later
            while stack and char < stack[-1] and last_occurrence[stack[-1]] > idx:
                removed = stack.pop()
                visited.remove(removed)

            # Add current character to the stack
            stack.append(char)
            visited.add(char)

        # Step 3: Return the result as a string
        return ''.join(stack)