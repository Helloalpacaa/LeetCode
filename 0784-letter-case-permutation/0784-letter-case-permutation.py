class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def generate(index: int, path: str) -> None:
            if len(path) == len(s):
                ans.append(path)
                return
            
            for i in range(index, len(s)):
                if s[i].isdigit():
                    generate(i + 1, path + s[i])
                else:
                    generate(i + 1, path + s[i].lower())
                    generate(i + 1, path + s[i].upper())
        
        generate(0, "")
        return ans