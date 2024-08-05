class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def isValid(segment: str) -> bool:
            return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)

        def backtracking(start: int, parts: List[str]) -> None:
            if len(parts) == 4 and start == len(s):
                ans.append('.'.join(parts))
                return
            
            if len(parts) == 4 or start == len(s):
                return
            
            for i in range(start, min(start + 3, len(s))):
                segment = s[start: i + 1]
                if isValid(segment):
                    parts.append(segment)
                    backtracking(i + 1, parts)
                    parts.pop()
        
        backtracking(0, [])
        return ans

