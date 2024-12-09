class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(left, right, path) -> None:
            if len(path) == n * 2:
                ans.append(path[:])
                return
            
            if left < n:
                generate(left + 1, right, path + '(')
            
            if right < left:
                generate(left, right + 1, path + ')')
        
        generate(0, 0, "")
        return ans