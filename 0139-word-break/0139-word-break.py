class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 1. transform wordDict to a set to we can check the existense with O(1)
        wordDict = set(wordDict)

        # dp[i]: ending with s[i - 1], if the string can be formed by the words in wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(dp)):
            for word in wordDict:
                if i >= len(word) and s[i - len(word): i] == word:
                    dp[i] = dp[i] or dp[i - len(word)]
        
        return dp[len(s)]