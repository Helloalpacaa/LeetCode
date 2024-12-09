class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            groups[sorted_word].append(word)
        
        ans = []
        for values in groups.values():
            ans.append(values)
        
        return ans