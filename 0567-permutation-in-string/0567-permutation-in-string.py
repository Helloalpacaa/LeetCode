class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        seen = Counter()
        
        for i in range(len(s2)):
            seen[s2[i]] += 1
            
            if i >= len(s1):
                if seen[s2[i - len(s1)]] > 1:
                    seen[s2[i - len(s1)]] -= 1
                else:
                    del seen[s2[i - len(s1)]]
            
            if seen == counter:
                return True
        
        return False