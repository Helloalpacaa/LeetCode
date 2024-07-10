class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        hm = {}
        for i in range(len(s)):
            hm[s[i]] = i
        
        ans = []
        i = 0
        while i < len(s):
            left = i
            j = hm[s[i]]
            while i <= j:
                j = max(j, hm[s[i]])
                i += 1
            ans.append(i - left)
        
        return ans