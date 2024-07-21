class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        for i in range(len(haystack)):
            while i + j < len(haystack) and haystack[i + j] == needle[j]:
                j += 1
                if j == len(needle):
                    return i
            j = 0
        
        return -1