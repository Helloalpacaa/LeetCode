class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []

        for word in words:
            if len(word) != len(pattern):
                continue
            
            n = len(word)
            word_hash = {}
            pattern_hash = {}
            for i in range(n):
                if word[i] in word_hash and word_hash[word[i]] != pattern[i] or pattern[i] in pattern_hash and pattern_hash[pattern[i]] != word[i]:
                    break
                
                word_hash[word[i]] = pattern[i]
                pattern_hash[pattern[i]] = word[i]
                if i == n - 1:
                    ans.append(word)
        
        return ans