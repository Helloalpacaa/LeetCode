class Solution:
    def romanToInt(self, s: str) -> int:
        roman = [[1, "I"], [5, "V"], [10, "X"], [50, "L"], [100, "C"], [500, "D"], [1000, "M"]]
        indexMap = {}
        for i in range(len(roman)):
            indexMap[roman[i][1]] = i
        
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if i < len(s) - 1 and indexMap[s[i + 1]] > indexMap[s[i]]:
                result -= roman[indexMap[s[i]]][0]
            else:
                result += roman[indexMap[s[i]]][0]
        
        return result