class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        start = len(s)

        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i - 1]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                start = i
        
        for i in range(start, len(s)):
            s[i] = '9'
        
        return int(''.join(s))