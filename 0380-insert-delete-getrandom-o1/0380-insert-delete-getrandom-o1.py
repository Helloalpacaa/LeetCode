class RandomizedSet:

    def __init__(self):
        self.numsArray = [] # array stores all the elements
        self.numsDict = {} # dict stores all the element: index in array
        

    def insert(self, val: int) -> bool:
        if val not in self.numsDict:
            self.numsArray.append(val)
            self.numsDict[val] = len(self.numsArray) - 1
            return True

        return False
        

    def remove(self, val: int) -> bool:
        if val in self.numsDict:
            index = self.numsDict[val]
            last_element = self.numsArray[-1]
            self.numsArray[index] = last_element
            self.numsArray.pop()
            self.numsDict[last_element] = index
            del self.numsDict[val]
            return True
        
        return False
        

    def getRandom(self) -> int:
        return self.numsArray[random.randint(0, len(self.numsArray) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()