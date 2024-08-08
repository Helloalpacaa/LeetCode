class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def isValid(s: str) -> bool:
            return len(s) == 1 or (len(s) > 1 and s[0] != '0' and int(s) <= 255)

        def backtracking(parts: List[str], index: int) -> None:
            if len(parts) == 4 and index == len(s):
                ans.append(".".join(parts[:]))
                return
            
            # 这步优化不能少
            if len(parts) == 4 or index == len(s):
                return

            for i in range(len(s)):
                if isValid(s[index: i + 1]):
                    parts.append(s[index: i + 1])
                    backtracking(parts, i + 1)
                    parts.pop()
        
        backtracking([], 0)
        return ans