class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i = 0
        j = len(tokens) - 1
        tokens.sort()
        score = 0
        ans = 0
        
        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                score += 1
                ans = max(ans, score)
                i += 1
            elif score > 0:
                power += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        
        return ans