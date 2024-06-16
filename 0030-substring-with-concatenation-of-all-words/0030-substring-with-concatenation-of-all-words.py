class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsCount = {}
        for word in words:
            wordsCount[word] = wordsCount.get(word, 0) + 1
        n = len(words)
        wordLen = len(words[0])
        ans = []
        
        for i in range(len(s) - wordLen * n + 1):
            substring = s[i: i + wordLen * n]
            if self.isConcat(substring, wordsCount, wordLen):
                ans.append(i)
        
        return ans
        
        
    def isConcat(self, s: str, wordsCount: Dict[str, int], wordLen) -> bool:
        seen = {}
        for i in range(0, len(s), wordLen):
            word = s[i : i + wordLen]
            seen[word] = seen.get(word, 0) + 1
            if word not in wordsCount or seen[word] > wordsCount[word]:
                return False
        
        return True
        
                