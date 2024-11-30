class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        start = strs[0]
        end = strs[-1]
        i = 0
        j = 0
        prefix = ""

        while i < len(start) and j < len(end):
            if start[i] != end[j]:
                break
            else:
                prefix += start[i]
                i += 1
                j += 1

        
        return prefix
            