class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = list(str(n))
        start = len(s)

        for i in range(len(s) - 1, 0, -1):
            if s[i] < s[i - 1]:
                s[i - 1] = str(int(s[i - 1]) - 1)
                start = i
        
        # 从最后一个变小了数字的之后一位开始 都改成9
        for i in range(start, len(s)):
            s[i] = '9'
        
        return int(''.join(s))