class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.collection = defaultdict(list)
        

    def insert(self, val: int) -> bool:
        res = False if val in self.collection else True
        self.arr.append(val)
        self.collection[val].append(len(self.arr) - 1)
        return res

    def remove(self, val: int) -> bool:
        if val not in self.collection:
            return False
        
        # print(self.collection)
        index = self.collection[val].pop() # remove the one at the last(most recent added)
        if not self.collection[val]:
            del self.collection[val]
        # 去移除arr里的这个val，如果它在中间，就把它和last_element换一下然后pop last element
        last_index = len(self.arr) - 1
        last_element = self.arr[last_index]

        # print(val, index, last_index, last_element, self.arr)
        if index == last_index:
            self.arr.pop()
        else:
            self.arr[index] = last_element
            self.arr.pop()
            self.collection[last_element].remove(last_index)
            self.collection[last_element].append(index)
        
        # print(val, index, last_index, last_element, self.arr)
        return True
        
    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()