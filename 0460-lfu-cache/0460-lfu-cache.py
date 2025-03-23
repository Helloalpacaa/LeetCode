class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.hashmap = {}
        self.freq = defaultdict(OrderedDict)
    
    def update_freq(self, key: int) -> None:
        value, freq = self.hashmap[key]

        del self.freq[freq][key]
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        self.freq[freq + 1][key] = None
        self.hashmap[key] = (value, freq + 1)
        
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        self.update_freq(key)
        return self.hashmap[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key] = (value, self.hashmap[key][1])
            self.update_freq(key)
        else:
            if len(self.hashmap) == self.capacity:
                lfu_key, _ = self.freq[self.min_freq].popitem(last=False)
                del self.hashmap[lfu_key]
            
            self.hashmap[key] = (value, 1)
            self.freq[1][key] = None
            self.min_freq = 1

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)