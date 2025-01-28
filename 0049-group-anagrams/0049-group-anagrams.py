class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for string in strs:
            key = "".join(sorted(list(string)))
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        
        ans = []
        for key in groups:
            ans.append(groups[key])
        
        return ans
            