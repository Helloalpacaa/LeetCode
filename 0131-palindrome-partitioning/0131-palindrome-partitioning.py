class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isValid(s: str, i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True
        
        def backtracking(path: List[str], index: int) -> None:
            if index == len(s):
                ans.append(path[:])
                return
            
            for i in range(index, len(s)):
                word = s[index: i + 1]
                if isValid(s, index, i):
                    path.append(word)
                    backtracking(path, i + 1)
                    path.pop()
            
        backtracking([], 0)
        return ans