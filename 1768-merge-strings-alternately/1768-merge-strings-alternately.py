class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merged = []
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                merged.append(word1[i])
                i += 1
                merged.append(word2[j])
                j += 1
            elif i < len(word1):
                merged.append(word1[i:])
                return "".join(merged)
            else:
                merged.append(word2[j:])
                return "".join(merged)
        
        return "".join(merged)
                
            