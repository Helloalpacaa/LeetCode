class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordsCount = {}
        for word in words:
            wordsCount[word] = wordsCount.get(word, 0) + 1
        wordlen = len(words[0])
        wordslen = len(words) * wordlen
        ans = []
        
        for i in range(len(s) - wordslen + 1):
            if self.isConcat(s[i: i + wordslen], wordsCount, wordlen):
                ans.append(i)
        
        return ans
        
        
    def isConcat(self, s: str, words: Dict[str, int], wordlen) -> bool:
        seen = {}
        for i in range(0, len(s), wordlen):
            currWord = s[i: i + wordlen]
            seen[currWord] = seen.get(currWord, 0) + 1
            if currWord not in words or seen[currWord] > words[currWord]:
                return False
        return True
        