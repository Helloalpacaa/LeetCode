class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] != abbr[j]:
                left = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                abbreviation = abbr[left: j]
                
                if not abbreviation or abbreviation[0] == '0':
                    return False
                
                i += int(abbreviation)
            else:
                i += 1
                j += 1
        
        return i == len(word) and j == len(abbr)