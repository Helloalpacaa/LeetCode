class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split()
        # s is no longer a string, but a list of strings. Each word is an element in this list.
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return " ".join(s)