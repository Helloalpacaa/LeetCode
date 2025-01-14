class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # build a doubly linkedlist to store the LRU at the tail, every Node stores (key, value)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # we need to move this key to the head of the Linkedlist
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.val
  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            LRU = self.tail.prev
            self.remove(LRU)
            del self.cache[LRU.key]

    
    # add new node right after head
    def add(self, node: Node) -> None:
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        
    
    # remove the LRU before the tail
    def remove(self, node) -> None:
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)