class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(open: int, close: int, path: str) -> None:
            if len(path) == n * 2:
                ans.append(path[:])
                return
            
            if open < n:
                backtracking(open + 1, close, path + "(")
            
            if close < open:
                backtracking(open, close + 1, path + ")")
        
        backtracking(0, 0, "")
        return ans