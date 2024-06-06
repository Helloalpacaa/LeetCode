class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        edge = {c: i for i, c in enumerate(s)} # using enumerate() to get both the index i and the character c, store the index as value and the character as the key in the dictionary
        
        ans = []
        left = 0
        right = 0
        for i, c in enumerate(s):
            right = max(right, edge[c])
            if i == right:
                ans.append(right - left + 1)
                left = right + 1
        
        return ans
        
        