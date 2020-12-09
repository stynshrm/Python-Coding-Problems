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

def print_List(curr):
    while curr:
        sep = ""
        print(str(curr.data) + " --> ", end = "")
        curr = curr.next


class FirstSolution:
    def reverseBetween(self, head, m, n):
        
        if not head:
            return None
        
        self.n = n
        self.m = m        
        self.p1 = None
        self.p2 = None
        
        def rec(i, cur):
            
            if i == self.n:
                self.p1 = cur
                self.p2 = cur.next
                return cur
           
            if i > self.m:
                n = rec(i+1, cur.next)
                n.next = cur           
                return cur
            
            
            if i == self.m:
                n = rec(i+1, cur.next)
                n.next = cur
                cur.next = self.p2
                return self.p1
            
            else:
                cur.next = rec(i+1, cur.next)
                return cur
        
     
        head = rec(1, head)
        
        return head



class SecondSolution:
    def reverseBetween(self, head, m, n):
        if m==n: return head
        
        def reverse(node, m, n):
            t2 = node
            if n > 1:
                if m > 1: 
                    node.next, t2 = reverse(node.next, m-1, n-1)
                else:
                    t1, t2 = reverse(node.next, m, n-1)
                    node.next = t2.next
                    t2.next = node
                    node, t2 = t1, node
            return node, t2
        return reverse(head, m, n)[0]

class thirdSolution:
    def reverseBetween(self, head, m,n):
        # dummy = Node(-1)
        # dummy.next = head
        pre = head
        for i in range(m-2):
            pre = pre.next
        cur = pre.next
        while (m < n):
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
            m += 1
        return head

slist = LinkedList()
slist.push(2)
slist.push(9)
slist.push(5)
slist.push(0)
slist.push(4)

print_List(slist.head)
print("")

it_Sol = thirdSolution()
result = it_Sol.reverseBetween(slist.head, 2, 5)
print_List(result)