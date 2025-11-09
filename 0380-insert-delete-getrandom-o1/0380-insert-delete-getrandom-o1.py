class RandomizedSet:

    def __init__(self):
        self.arr = [] # store the number
        self.num_to_idx = {} # store num:(index in self.arr)
        

    def insert(self, val: int) -> bool:
        if val in self.num_to_idx:
            return False
        self.arr.append(val)
        self.num_to_idx[val] = len(self.arr) - 1

    def remove(self, val: int) -> bool:
        if val not in self.num_to_idx:
            return False
        
        last_element = self.arr[-1]
        last_idx = len(self.arr) - 1
        idx = self.num_to_idx[val]
        if idx != last_idx:
            self.arr[idx] = last_element
            self.num_to_idx[last_element] = idx
        self.arr.pop()
        del self.num_to_idx[val]

        return True
        

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()