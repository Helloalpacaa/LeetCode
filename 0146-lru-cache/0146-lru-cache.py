class Node:

    def __init__(self, key: int, val: int):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # 把这个node从原本在linkedlist里的位置移到head后面
        self.remove(node)
        self.add(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.add(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                LRU = self.tail.prev
                self.remove(LRU)
                del self.cache[LRU.key]


    def remove(self, node: Node) -> None:
        next_node = node.next
        prev = node.prev
        prev.next = next_node
        next_node.prev = prev
    
    def add(self, node: Node) -> None:
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)