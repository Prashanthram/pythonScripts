class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head = node()
    def isEmpty(self):
        if self.head.next == None:
            return True
        else: return False
    def addNode(self,data):
        newNode = node(data)
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
        curNode.next = newNode
    def display(self):
        ele =[]
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
            ele.append(curNode.data)
        print(ele)
l = linkedList()
l.addNode(6)
l.addNode(5)
l.addNode(4)
l.addNode(3)
l.addNode(2)
l.display()
l1 = linkedList()
l1.addNode(5)
print(l1.isEmpty())