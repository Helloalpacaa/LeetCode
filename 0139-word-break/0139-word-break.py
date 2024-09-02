class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordDictSet = set(wordDict)

        # i用来iterate s
        for i in range(n):
            if dp[i]:
                for j in range(i + 1, n + 1):
                    if s[i: j] in wordDictSet:
                        dp[j] = True
        
        return dp[n]
