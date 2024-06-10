class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        edge = {}
        for index, value in enumerate(s):
            edge[value] = index
        
        ans = []
        left = 0
        right = 0
        for i in range(len(s)):
            right = max(right, edge[s[i]])
            if i == right:
                ans.append(right - left + 1)
                left = right + 1
        
        return ans
            