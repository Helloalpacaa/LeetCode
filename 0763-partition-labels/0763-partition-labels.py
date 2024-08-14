class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = i
        
        left, right = 0, 0
        ans = []
        for i in range(len(s)):
            right = max(right, hashmap[s[i]])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        
        return ans
