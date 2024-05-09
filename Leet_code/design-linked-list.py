class ListNode:
    
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
            
        return -1

        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode
        


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
       


    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        i = 0
        curr = self.head

        while i < index and curr:
            i+=1
            curr = curr.next
        
        if curr:
            newNode.next = curr.next
            curr.next = newNode
            if not newNode.next:
                self.tail = newNode
        
        

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head

        while i < index and curr:
            i+=1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
        
    

        


