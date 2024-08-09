class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []

        def backtracking(index: int, path: str) -> None:
            if len(path) == len(digits) and len(digits) != 0:
                ans.append(path[:])
                return
            
            for i in range(index, len(digits)):
                digit = int(digits[index])
                for letter in letters[digit]:
                    backtracking(i + 1, path + letter)
            
        backtracking(0, "")
        return ans