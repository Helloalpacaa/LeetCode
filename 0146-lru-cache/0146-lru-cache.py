class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # stores (key, node) pair where node is a (key, value) pair
        self.head = Node(0, 0) # dummy head node
        self.tail = Node(0, 0) # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, node: Node):
        # add new node right after Head
        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        node.prev = self.head
        nextNode.prev = node
    
    def remove(self, node: Node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key] # get the node from self.cache
            self.remove(node) # remove the node from it's oroginal place in the linkedlist
            self.add(node) # add the node right after the head
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # 移除掉原来的node
        node = Node(key, value) # 新建一个node
        self.add(node) # 把node加进head之后
        self.cache[key] = node # 把node加进hashmap
        
        if len(self.cache) > self.capacity:
            lru = self.tail.prev # linkedlist的tail的前一位是least recently used，把它从linkedlist中移除
            self.remove(lru) 
            del self.cache[lru.key] # 把lru也从hashmap里移出

            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)