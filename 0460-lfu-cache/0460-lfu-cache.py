class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.freq = defaultdict(OrderedDict)
        self.min_freq = 1
    
    def update_freq(self, key: int) -> None:
        # get the value and freq
        value, freq = self.map[key]
        # increment the freq by 1
        self.map[key] = value, freq + 1

        # remove key from self.freq[freq], add it into self.freq[freq + 1]
        del self.freq[freq][key]
        # if the freq doesn't exist anymore, check if self.min_freq == freq, if it is, increment self.min_freq
        if not self.freq[freq]:
            del self.freq[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        # Add the key into new freq + 1
        self.freq[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        
        self.update_freq(key)
        return self.map[key][0]
        
    def put(self, key: int, value: int) -> None:
        # if key in map, we just need to update its frequency
        if key in self.map:
            self.update_freq(key)
        # we need to add the new key in map
        else:
            # if there is no space, we need to pop the LRU in self.freq[self.min_freq]
            if len(self.map) == self.capacity:
                lfu_key, _ = self.freq[self.min_freq].popitem(last=False)
                del self.map[lfu_key]

            self.map[key] = value, 1
            self.freq[1][key] = None
            self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)