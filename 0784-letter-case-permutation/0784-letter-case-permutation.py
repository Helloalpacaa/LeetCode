class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtracking(path: List[str], index: int) -> None:
            if len(path) == len(s):
                ans.append("".join(path[:]))
                return
            
            if s[index].isdigit():
                path.append(s[index])
                backtracking(path, index + 1)
                path.pop() # 这里的pop()必须有，因为要一直回溯到一开始，如果中间有一个数字不回溯，就没法回溯到这个数字之前的字母
            else:
                path.append(s[index].lower())
                backtracking(path, index + 1)
                path.pop()

                path.append(s[index].upper())
                backtracking(path, index + 1)
                path.pop()
        
        backtracking([], 0)
        return ans

                
                
                