class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 把每个size为k的不同的substring加进一个set里，最终检查set的数量
        substrings = set()

        for i in range(0, len(s) - k):
            substrings.add(s[i: i + k])
        
        return len(substrings) == 2 ** k
