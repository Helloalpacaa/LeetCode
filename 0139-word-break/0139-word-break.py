class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if s[j - 1: i] in wordSet and dp[j - 1]:
                    dp[i] = True

        return dp[n]