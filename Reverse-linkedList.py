class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_Node = Node(new_data)
        new_Node.next = self.head
        self.head = new_Node

    def printList(self):
        curr = self.head
        while curr:
            print(str(curr.data) + " --> ", end = "")
            curr = curr.next

    def reverseList(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def rec_reverseList(self):
        def _helper(curr, prev):
            if not curr:
                return prev

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next            
            return _helper(curr, prev)

        self.head = _helper(curr=self.head, prev = None)


list = LinkedList()
list.push(2)
list.push(9)
list.push(5)
list.push(4)

list.printList()
print("")
print("Reversed List")
list.reverseList()
list.printList()
print("")
print("Again Reversed  back")
list.rec_reverseList()
list.printList()