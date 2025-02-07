class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count_one = 0
        flip = 0

        for char in s:
            if char == '1':
                count_one += 1
            else:
                flip = min(count_one, flip + 1)
        
        return flip