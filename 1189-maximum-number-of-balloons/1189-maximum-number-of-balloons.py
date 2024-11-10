class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = dict()
        for char in text:
            if char in "ban":
                count[char] = count.get(char, 0) + 1
            elif char in "lo":
                count[char] = count.get(char, 0) + 0.5

        maxNumber = float('inf')
        for char in "balloon":
            if char not in count:
                return 0
            maxNumber = min(maxNumber, count[char])
        
        return int(maxNumber)