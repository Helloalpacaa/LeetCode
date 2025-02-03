class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []

        if len(digits) == 0:
            return ans

        def backtracking(start, path) -> None:
            if len(path) == len(digits):
                ans.append(path)
                return
            
            for i in range(start, len(digits)):
                digit = digits[i]
                word = digits_map[ord(digit) - ord('0')]

                for char in word:
                    backtracking(i + 1, path + char)
        
        backtracking(0, "")
        return ans