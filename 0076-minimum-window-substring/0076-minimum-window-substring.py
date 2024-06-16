class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = {}
        for c in t:
            hashmap[c] = hashmap.get(c, 0) + 1
        size = len(hashmap)
        i = 0
        windowSize = float('inf')
        ans = ""
        
        for j in range(len(s)):
            if s[j] in hashmap:
                hashmap[s[j]] -= 1
                if hashmap[s[j]] == 0:
                    size -= 1
            
            while size == 0:
                if windowSize > j - i + 1:
                    windowSize = j - i + 1
                    ans = s[i :j + 1]
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    if hashmap[s[i]] > 0: # 这个条件一定要有
                        size += 1
                i += 1
        
        return ans
        
        
        