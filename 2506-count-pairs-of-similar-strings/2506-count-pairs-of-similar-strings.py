class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # for each word, get its sorted str without repeating letters, store it in a hashmap (str, freq)
        hm = {}
        for word in words:
            key = "".join(sorted(set(word)))
            hm[key] = hm.get(key, 0) + 1
        
        # iterate the value in the hashmap, count the number of pairs if can form
        pairs = 0
        for value in hm.values():
            pairs += (value * (value - 1)) // 2

        return pairs
