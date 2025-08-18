class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        ans = []

        for part in parts:
            if part == '..':
                if ans:
                    ans.pop()
            elif part != '' and part != '.':
                ans.append(part)
        
        return '/' + "/".join(ans)