class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashmap = {}
        i = 0
        ans = 0
        
        for j in range(len(s)):
            hashmap[s[j]] = hashmap.get(s[j], 0) + 1
            
            while len(hashmap) > 2:
                hashmap[s[i]] -= 1
                if hashmap[s[i]] == 0:
                    hashmap.pop(s[i])
                i += 1
                    
            ans = max(ans, j - i + 1)
        
        return ans