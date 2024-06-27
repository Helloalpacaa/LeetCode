class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = 0
        counter = Counter()
        i = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            
            while len(counter) > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
                
            
            longest = max(longest, j - i + 1)
        
        return longest