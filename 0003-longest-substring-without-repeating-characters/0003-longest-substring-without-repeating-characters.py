class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        n = len(s)
        window = set()

        # two pointers
        i = 0
        for j in range(n):
            char = s[j]
            while char in window:
                window.remove(s[i])
                i += 1
            
            window.add(char)
            longest = max(longest, len(window))
        
        return longest
