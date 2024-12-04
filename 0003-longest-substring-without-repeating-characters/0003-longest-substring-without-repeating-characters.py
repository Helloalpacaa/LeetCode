class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Using a sliding window to maintain the characters in substring
        window = set()

        # Use two pointers to maintain the range of the substring
        # Every time we move right 1 element forward
        left = 0
        longest = 0
        for right in range(len(s)):
            char = s[right]

            # while there is repeating characters in the window, we move left pointer
            while char in window:
                window.remove(s[left])
                left += 1
            
            # add current char into the sliding window
            window.add(char)
            
            # update the longest if needed
            longest = max(longest, right - left + 1)
        
        return longest

            
