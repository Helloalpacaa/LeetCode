class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        ans = 0
        counter = {c: 0 for c in "abc"}
        
        for j in range(len(s)):
            counter[s[j]] += 1
            
            while all(counter.values()):
                counter[s[i]] -= 1
                i += 1
                
            ans += i
        
        return ans