class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(left, right, parenthesis) -> None:
            if len(parenthesis) == n * 2:
                ans.append(parenthesis)
            
            if left < n:
                generate(left + 1, right, parenthesis + "(")
            
            if right < left:
                generate(left, right + 1, parenthesis + ")")
        
        generate(0, 0, "")
        return ans
            

