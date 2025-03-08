class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        index = -1

        for i in range(len(s) - 1, -1, -1):
            if count[s[i]] == 1:
                index = i
        
        return index
