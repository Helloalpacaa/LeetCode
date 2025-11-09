class Node:

    def __init__(self, val: int, min: int, next: None):
        self.val = val
        self.min = min
        self.next = next

class MinStack:

    def __init__(self):
        self.head = None
        

    def push(self, val: int) -> None:
        node = Node(val, min(val, self.head.min) if self.head else val, self.head)
        self.head = node
        

    def pop(self) -> None:
        self.head = self.head.next
        

    def top(self) -> int:
        return self.head.val
        

    def getMin(self) -> int:
        return self.head.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()