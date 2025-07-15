class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                diff = 26 + ord(s[i + 1]) - ord(s[i])
                key += (diff % 26,)
            group[key].append(s)
        
        return list(group.values())
