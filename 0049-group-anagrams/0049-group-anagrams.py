class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for word in strs:
            original = word
            word = "".join(sorted(word))
            group[word].append(original)
        
        ans = []
        for key in group:
            ans.append(group[key])
        
        return ans

