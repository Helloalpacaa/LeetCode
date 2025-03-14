class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordDict = set(wordDict)

        def backtracking(startIdx: int, path: List[str]) -> None:
            if startIdx == len(s):
                ans.append(" ".join(path[:]))
                return
            
            for i in range(startIdx, len(s)):
                word = s[startIdx: i + 1]
                if word in wordDict:
                    path.append(word)
                    backtracking(i + 1, path)
                    path.pop()
        
        backtracking(0, [])
        return ans