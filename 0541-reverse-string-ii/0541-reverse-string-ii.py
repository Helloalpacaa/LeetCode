class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        
        def reverse(string, i, j):
            while i < j:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
            
        for i in range(0, len(s), k * 2):
            reverse(s, i, min(i + k - 1, len(s) - 1))
        
        return ''.join(s)