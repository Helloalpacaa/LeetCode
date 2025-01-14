class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # calculate the frequency of all words in words2
        freq = {}

        for word in words2:
            count = Counter(word)
            for char in count:
                if char not in freq or freq[char] < count[char]:
                    freq[char] = count[char]
        
        ans = []
        for word in words1:
            count = Counter(word)

            if all(count[char] >= freq[char] for char in freq):
                ans.append(word)
        
        return ans