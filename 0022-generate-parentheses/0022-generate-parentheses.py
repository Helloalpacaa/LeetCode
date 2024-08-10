class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(left: int, right: int, path: str) -> None:
            if len(path) == n * 2:
                ans.append(path[:])
                return
            
            if left == right:
                generate(left + 1, right, path + "(")
            elif left > right:
                if left < n:
                    generate(left + 1, right, path + "(")
                    generate(left, right + 1, path + ")")
                else:
                    generate(left, right + 1, path + ")")
        
        generate(0, 0, "")
        return ans
