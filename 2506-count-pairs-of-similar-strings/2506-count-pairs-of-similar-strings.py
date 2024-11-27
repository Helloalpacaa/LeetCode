class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordsMap = {}
        count = 0
        for word in words:
            word = sorted(set(word))
            word = "".join(word)
            wordsMap[word] = wordsMap.get(word, 0) + 1
            count = max(count, wordsMap[word])

        return count if count > 1 else 0