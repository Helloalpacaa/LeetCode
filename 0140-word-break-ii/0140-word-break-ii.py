class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        res = []
        memo = {}

        def dfs(start: int) -> list[str]:
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]
            
            sentences = []

            for end in range(start + 1, len(s) + 1):
                word = s[start: end]
                if word in wordset:
                    for sub in dfs(end):
                        if sub:
                            # when sub has something
                            sentences.append(word + " " + sub)
                        else:
                            # when sub is ""
                            sentences.append(word)
            
            memo[start] = sentences
            return sentences
        
        return dfs(0)

