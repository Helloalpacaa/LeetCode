class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        edges = {}
        for i in range(len(s)):
            edges[s[i]] = i
        
        left = 0
        right = 0
        ans = []
        for i in range(len(s)):
            right = max(right, edges[s[i]])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        
        return ans