class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # Two pointers, use i to iterate p, j iterate s, move i when p[i] == s[j]
        # if i can reach the end of p, when we find a match

        i = 0
        j = 0
        while i < len(p) and j < len(s):
            if p[i] == s[j]:
                i += 1
                j += 1
            elif p[i] == '*':
                i += 1
            else:
                j += 1

        while i < len(p) and p[i] == '*':
            i += 1

        return i == len(p)