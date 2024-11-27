class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     word = strs[i]
        #     i = 0
        #     j = 0
        #     while i < len(prefix) and j < len(word) and prefix[i] == word[j]:
        #         i += 1
        #         j += 1
        #     prefix = list(prefix)
        #     prefix = "".join(prefix[:i])
        #     if prefix == "":
        #         break
        
        # return prefix

        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        j = 0
        ans = ""
        while i < len(first) and j < len(last):
            if first[i] == last[j]:
                ans += first[i]
                i += 1
                j += 1
            else:
                break
        
        return ans