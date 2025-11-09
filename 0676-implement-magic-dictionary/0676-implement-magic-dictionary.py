class MagicDictionary:

    def __init__(self):
        self.pattern = defaultdict(list)
        
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i + 1:]
                self.pattern[p].append(word)
        

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            p = searchWord[:i] + "*" + searchWord[i + 1:]
            if p in self.pattern:
                for pa in self.pattern[p]:
                    if pa != searchWord:
                        return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)