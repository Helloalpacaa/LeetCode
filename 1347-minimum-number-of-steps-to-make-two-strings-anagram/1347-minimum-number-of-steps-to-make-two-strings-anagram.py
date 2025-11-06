class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0
        for c in count_s:
            if count_s[c] > count_t[c]:
                steps += count_s[c] - count_t[c]
        
        return steps