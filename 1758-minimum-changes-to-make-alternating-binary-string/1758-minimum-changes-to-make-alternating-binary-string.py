class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(n):
            if int(s[i]) != i % 2:
                count += 1
        
        return min(count, n - count)