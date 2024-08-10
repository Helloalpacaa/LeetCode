class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def generate(index: int, path: str) -> None:
            if len(path) == len(s):
                ans.append(path)
                return
            
            
            if s[index].isdigit():
                generate(index + 1, path + s[index])
            else:
                generate(index + 1, path + s[index].lower())
                generate(index + 1, path + s[index].upper())
        
        generate(0, "")
        return ans