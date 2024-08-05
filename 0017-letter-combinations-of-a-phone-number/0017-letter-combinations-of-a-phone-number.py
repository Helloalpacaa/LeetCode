class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        words = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []

        if len(digits) == 0:
            return ans

        def backtracking(startIdx: int, path: List[str]) -> None:
            if len(path) == len(digits):
                ans.append("".join(path[:]))
                return
            
            digit = int(digits[startIdx])

            for char in words[digit]:
                path.append(char)
                backtracking(startIdx + 1, path)
                path.pop()
        
        backtracking(0, [])
        return ans