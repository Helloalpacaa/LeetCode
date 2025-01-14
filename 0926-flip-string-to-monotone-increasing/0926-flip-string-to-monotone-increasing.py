class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        counter_flip = 0
        counter_one = 0

        for char in s:
            if char == '1':
                counter_one += 1
            else:
                counter_flip = min(counter_one, counter_flip + 1)
        
        return counter_flip