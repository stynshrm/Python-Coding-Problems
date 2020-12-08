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

    # Recursive solution 1
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
    
    # Recursive solution 2
    def rev_rec(self):
        def rrevList(curr):
            if (curr == None or curr.next == None):
                return curr    
            newHead = rrevList(curr.next) 
            curr.next.next= curr
            curr.next = None
            return newHead
        self.head = rrevList(self.head)


def rrevList(curr):
    if (curr == None or curr.next == None):
        return curr    
    newHead = rrevList(curr.next) 
    curr.next.next= curr
    curr.next = None
    return newHead

def print_List(curr):
    while curr:
        sep = ""
        print(str(curr.data) + " --> ", end = "")
        curr = curr.next

slist = LinkedList()
slist.push(2)
slist.push(9)
slist.push(5)
slist.push(4)

slist.printList()
print("")
# a = rrevList(slist.head)
# print_List(a)
slist.rev_rec()
slist.printList()
