class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p_map = {}
        window_map = {}
        
        for char in p:
            p_map[char] = p_map.get(char, 0) + 1
        
        for i in range(len(s)):
            window_map[s[i]] = window_map.get(s[i], 0) + 1
            
            if i >= len(p):
                window_map[s[i - len(p)]] -= 1
                if window_map[s[i - len(p)]] == 0:
                    del window_map[s[i - len(p)]]
            
            if window_map == p_map:
                ans.append(i - len(p) + 1)
        
        return ans