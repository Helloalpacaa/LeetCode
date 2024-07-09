class Node:
    
    def __init__(self, val: 0, next: None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        newHead = Node(val, None)
        newHead.next = self.head
        self.head = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index > self.size:
            return
        else:
            newNode = Node(val, None)
            dummy = Node(0, self.head)
            curr = dummy

            for _ in range(index):
                curr = curr.next

            newNode.next = curr.next
            curr.next = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        dummy = Node(0, self.head)
        curr = dummy
        
        for _ in range(index):
            curr = curr.next
            
        curr.next = curr.next.next
        self.head = dummy.next # 这一条很重要，如果index为1的话就要更新新的head
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)