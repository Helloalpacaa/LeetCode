class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordset = set(words)
        memo = {}

        def can_form(word: str) -> bool:
            if word == "":
                return False
            
            if word in memo:
                return memo[word]
            
            for i in range(len(word)):
                prefix, suffix = word[ : i + 1], word[i + 1 : ]
                if prefix in wordset and (suffix in wordset or can_form(suffix)):
                    memo[word] = True
                    return True
            
            memo[word] = False
            return False
        
        ans = []
        for word in words:
            if can_form(word):
                ans.append(word)
        
        return ans

