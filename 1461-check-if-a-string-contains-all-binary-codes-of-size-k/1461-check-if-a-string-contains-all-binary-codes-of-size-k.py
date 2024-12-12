class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 把每个size为k的不同的substring加进一个set里，最终检查set的数量
        substrings = set()
        substring = ""

        for i in range(len(s)):
            substring += s[i]

            if i >= k:
                substring = s[i - k + 1: i + 1]
            
            if len(substring) == k:
                substrings.add(substring)
        
        return len(substrings) == 2 ** k
