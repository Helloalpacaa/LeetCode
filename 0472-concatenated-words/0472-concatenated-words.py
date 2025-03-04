class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        ans = []

        for word in words:
            n = len(word)
            dp = [0] * (n + 1)
            dp[0] = 1

            for i in range(1, n + 1):
                # for w in words_set:
                #     if i >= len(w) and dp[i - len(w)] == 1 and word[i - len(w): i] == w:
                #         dp[i] += 1
                for j in range(0, i):
                    if dp[j] > 0 and word[j: i] in words_set:
                        dp[i] = dp[j] + 1
            
            if dp[n] >= 3:
                ans.append(word)
        
        return ans
