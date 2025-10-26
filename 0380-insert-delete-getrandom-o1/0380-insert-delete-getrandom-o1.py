class RandomizedSet:

    def __init__(self):
        self.arr = [] # store the value
        self.hashmap = {} # store value: index
        

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        self.arr.append(val)
        index = len(self.arr) - 1
        self.hashmap[val] = index

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        
        index = self.hashmap[val]
        del self.hashmap[val]
        last_index = len(self.arr) - 1
        last_element = self.arr[last_index]
        if last_index != index:
            self.arr[index] = last_element
            self.hashmap[last_element] = index
        self.arr.pop()

        return True
        

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()