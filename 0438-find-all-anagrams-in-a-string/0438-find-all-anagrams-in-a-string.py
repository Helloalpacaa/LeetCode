class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        window = Counter()
        ans = []
        
        for i in range(len(s)):
            window[s[i]] += 1
            
            if i >= len(p):
                if window[s[i - len(p)]] == 1:
                    del window[s[i - len(p)]]
                else:
                    window[s[i - len(p)]] -= 1
            
            if window == counter:
                ans.append(i - len(p) + 1)
        
        return ans