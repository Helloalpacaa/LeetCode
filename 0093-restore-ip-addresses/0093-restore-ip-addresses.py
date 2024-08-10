class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def isValid(s: str) -> bool:
            return len(s) == 1 or s[0] != "0" and int(s) <= 255
        
        def backtracking(index: int, parts: List[str]) -> None:
            if len(parts) == 4 and index == len(s):
                ans.append(".".join(parts))
                return
            
            for i in range(index, len(s)):
                substring = s[index: i + 1]
                if isValid(substring):
                    parts.append(substring)
                    backtracking(i + 1, parts)
                    parts.pop()

        backtracking(0, [])
        return ans
