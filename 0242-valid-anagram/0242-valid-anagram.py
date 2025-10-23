class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = defaultdict(int)

        for c in t:
            t_count[c] += 1
            if t_count[c] > s_count[c]:
                return False
        
        return t_count == s_count