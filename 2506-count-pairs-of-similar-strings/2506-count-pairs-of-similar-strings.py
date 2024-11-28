class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordsMap = {}
        for word in words:
            word = "".join(sorted(set(word)))
            wordsMap[word] = wordsMap.get(word, 0) + 1

        pairs = 0
        for count in wordsMap.values():
            if count > 1:
                pairs += (count * (count - 1)) // 2
        
        return pairs