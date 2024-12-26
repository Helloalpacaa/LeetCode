class Solution:
    def maxSubstringLength(self, s: str) -> int:
        n = len(s)
        first_occur = {}
        last_occur = {}
        for index, char in enumerate(s):
            if char not in first_occur:
                first_occur[char] = index
            last_occur[char] = index
        
        max_length = -1
        for char, i in first_occur.items():
            right_most = last_occur[char]
            for j in range(i, n):
                left, right = first_occur[s[j]], last_occur[s[j]]
                if left < i:
                    break
                right_most = max(right_most, right)
                if j == right_most and j - i + 1 < n:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
