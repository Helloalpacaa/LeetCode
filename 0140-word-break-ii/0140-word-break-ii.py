class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        res = []

        def dfs(word_index: str, path: list[str]) -> None:
            if word_index == len(s):
                res.append(" ".join(path))
                return
            
            for i in range(word_index, len(s)):
                word = s[word_index: i + 1]
                if word in wordset:
                    path.append(word)
                    dfs(i + 1, path)
                    path.pop()
        
        dfs(0, [])
        return res


