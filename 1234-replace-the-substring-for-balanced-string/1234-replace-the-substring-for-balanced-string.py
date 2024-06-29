class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        i = 0
        ans = float('inf')
        
        for j in range(len(s)):
            counter[s[j]] -= 1
            
            while i < len(s) and all(len(s) / 4 >= counter[c] for c in "QWER"):
                ans = min(ans, j - i + 1)
                counter[s[i]] += 1
                i += 1
        
        return ans