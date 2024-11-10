class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(left, right, path) -> None:
            if len(path) == 2 * n:
                ans.append(path[:])
                return
            
            if left < n:
                backtracking(left + 1, right, path + '(')
            if right < left:
                backtracking(left, right + 1, path + ')')
        
        backtracking(0, 0, "")
        return ans
            
