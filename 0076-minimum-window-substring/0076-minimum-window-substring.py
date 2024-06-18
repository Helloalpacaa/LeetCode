class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        n = len(counter)
        ans = ""
        i = 0
        match = 0
        
        for j in range(len(s)):
            if s[j] in counter:
                counter[s[j]] -= 1
                if counter[s[j]] == 0:
                    match += 1
            
            while match == n:
                if not ans or j - i + 1 < len(ans):
                    ans = s[i : j + 1]
                    
                if s[i] in counter:
                    counter[s[i]] += 1
                if counter[s[i]] > 0:
                    match -= 1
                i += 1
            
        return ans
                