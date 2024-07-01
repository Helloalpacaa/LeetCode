class Solution:
    def balancedString(self, s: str) -> int:
        i = 0
        ans = float('inf')
        counter = Counter(s)
        n = len(s)
        
        for j in range(n):
            counter[s[j]] -= 1
            
            while i < n and all(n / 4 >= counter[c] for c in "QWER"):
                ans = min(ans, j - i + 1)
                counter[s[i]] += 1
                i += 1
            
        return ans
                