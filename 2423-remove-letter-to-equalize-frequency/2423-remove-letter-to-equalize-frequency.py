class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)
        freq_of_count = Counter(count.values())

        if len(freq_of_count) == 1:
            # 所有字母频率相同
            # 只有一个字母：3: 1
            if 1 in freq_of_count.values():
                return True
            # 有多个字母但每个只出现一次
            if list(freq_of_count.keys())[0] == 1:
                return True
        
        if len(freq_of_count) == 2:
            (f1, c1), (f2, c2) = sorted(freq_of_count.items())

            if f2 == f1 + 1 and c2 == 1:
                return True
            
            if f1 == 1 and c1 == 1:
                return True
            
        
        return False
