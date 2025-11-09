class MagicDictionary:

    def __init__(self):
        self.dict_by_length = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.dict_by_length[len(word)].append(word)
        

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.dict_by_length:
            return False
        
        for word in self.dict_by_length[len(searchWord)]:
            diff = sum(searchWord[i] != word[i] for i in range(len(word)))
            if diff == 1:
                return True
        
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)