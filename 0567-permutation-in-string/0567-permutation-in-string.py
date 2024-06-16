class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        match = 0
        
        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
                if counter[s2[i]] == 0:
                    match += 1
            
            if i >= len(s1) and s2[i - len(s1)] in counter:
                if counter[s2[i - len(s1)]] == 0:
                    match -= 1
                counter[s2[i - len(s1)]] += 1
            
            if match == len(counter):
                return True
        
        return False