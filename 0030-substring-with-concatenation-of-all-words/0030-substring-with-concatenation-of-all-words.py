class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = {}
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        wordLen = len(words[0])
        wordsLen = wordLen * len(words)
        ans = []
        
        for i in range(len(s) - wordsLen + 1):
            if self.isConcat(s[i: i + wordsLen], counter, wordLen):
                ans.append(i)
        return ans
        
        
    
    def isConcat(self, s: str, words: Dict[str, int], wordLen) -> bool:
        seen = {}
        for i in range(0, len(s), wordLen):
            currWord = s[i: i + wordLen]
            seen[currWord] = seen.get(currWord, 0) + 1
            if currWord not in words or seen[currWord] > words[currWord]:
                return False
        return True
        
        