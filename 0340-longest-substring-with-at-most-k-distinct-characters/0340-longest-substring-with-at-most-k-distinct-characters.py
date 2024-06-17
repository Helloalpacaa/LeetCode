class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = Counter()
        ans = 0
        i = 0
        
        # 这个解法最直观 不需要去更改k的值
        for j in range(len(s)):
            counter[s[j]] += 1
            
            if len(counter) <= k:
                ans = max(ans, j - i + 1)
                
            while len(counter) > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
        
        return ans
            