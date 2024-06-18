class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        counter = {c: 0 for c in 'abc'}
        
        for j in range(len(s)):
            counter[s[j]] += 1
            
            while all(counter.values()): # while all the values in counter are  > 0
                counter[s[i]] -= 1
                i += 1
            
            ans += i
            
        return ans
                    