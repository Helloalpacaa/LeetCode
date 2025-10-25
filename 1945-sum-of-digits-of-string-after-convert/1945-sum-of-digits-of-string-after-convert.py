class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_str = "".join(str(ord(ch) - ord('a') + 1) for ch in s)
        
        for _ in range(k):
            total = 0
            for c in num_str:
                total += int(c)
            num_str = str(total)
        
        return total