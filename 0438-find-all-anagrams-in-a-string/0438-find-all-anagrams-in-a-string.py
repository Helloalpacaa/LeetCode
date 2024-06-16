class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        match = 0
        ans = []
        
        for i in range(len(s)):
            if s[i] in counter:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    match += 1
            
            if i >= len(p) and s[i - len(p)] in counter:
                if counter[s[i - len(p)]] == 0:
                    match -= 1
                counter[s[i - len(p)]] += 1
            
            if match == len(counter):
                ans.append(i - len(p) + 1)
        
        return ans
            
            