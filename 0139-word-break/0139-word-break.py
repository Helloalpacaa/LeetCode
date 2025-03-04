class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        # for i in range(1, n + 1):
        #     for j in range(0, i):
        #         if dp[j] and s[j: i] in wordDict:
        #             dp[i] = True
        
        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word): i] == word:
                    dp[i] = True

        return dp[n]