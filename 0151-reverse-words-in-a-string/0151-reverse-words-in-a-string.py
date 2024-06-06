class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # Remove leading and trailing whitespace
        words = s.split() # split the string into words
        
        left = 0
        right = len(words) - 1
        
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        
        return ' '.join(words)
        
        