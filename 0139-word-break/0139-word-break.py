class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        left = 0
        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word): i] == word:
                    dp[i] = True
        
        return dp[n]