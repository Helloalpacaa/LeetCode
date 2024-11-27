class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            i = 0
            j = 0
            while i < len(prefix) and j < len(word) and prefix[i] == word[j]:
                i += 1
                j += 1
            prefix = list(prefix)
            prefix = "".join(prefix[:i])
            if prefix == "":
                break
        
        return prefix