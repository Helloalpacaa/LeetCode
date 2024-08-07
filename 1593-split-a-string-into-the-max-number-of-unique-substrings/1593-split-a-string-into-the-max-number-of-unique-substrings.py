class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.maxSplit = 0

        def backtracking(path: List[str], startIdx: int) -> None:
            if startIdx == len(s):
                self.maxSplit = max(self.maxSplit, len(path))
                return
            
            for i in range(startIdx, len(s)):
                word = s[startIdx: i + 1]
                if word not in path:
                    path.append(word)
                    backtracking(path, i + 1)
                    path.pop()
        
        backtracking([], 0)
        return self.maxSplit