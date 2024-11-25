class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head =None

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if current is None:
                return -1
            current = current.next
        return current.val if current else -1

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if self.head is None:
            self.head = new
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        new = Node(val)
        if index ==0:
            self.addAtHead(val)
            return
        
        current = self.head
        for i in range(index-1):
            if current is None:
                return
            current =current.next
        if current is None:
            return
        new.next = current.next
        current.next = new
        
        

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index==0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index-1):
            if current is None or current.next is None:
                return
            current = current.next
            
        if current.next is None:
            return
        
        current.next = current.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)