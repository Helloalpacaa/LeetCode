class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        n = len(s)
        counter = Counter("abc")
        match = 0
        
        for j in range(n):
            if s[j] in counter:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    match += 1
            
            while match == 3:
                ans += (n - j)
                if s[i] in counter:
                    counter[s[i]] += 1
                if counter[s[i]] > 0:
                    match -= 1
                i += 1
            
        return ans
                    