class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = 0
        count = defaultdict(int)
        left = 0

        for right in range(len(s)):
            c = s[right]
            count[c] += 1

            while count[c] > 1:
                count[s[left]] -= 1
                left += 1
            
            window = max(window, right - left + 1)
        
        return window