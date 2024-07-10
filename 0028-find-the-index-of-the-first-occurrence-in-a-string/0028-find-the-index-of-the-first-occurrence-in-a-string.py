class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        for i in range(len(haystack)):
            j = 0
            while i + j < len(haystack) and j < len(needle) and haystack[i + j] == needle[j]:
                j += 1
            
            if j == len(needle):
                return i
        
        return -1