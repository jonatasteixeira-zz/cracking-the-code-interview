# Cracking the code interview 
#
# 3.2 - Stack Min
# How would you design a stack which, in addiction to push and pop,  has a function min
# which return the minimun element? Push, pop and min should all operate O(1) timne.

class Stack:
    class Node:
        def __init__(self, data = None):
            self.data = data
            self.prev = None
    
    def __init__(self):
        self.head = None
        self.min = None
        self.size = 0
    
    def push(self, data):
        node = self.Node(data)
        if(self.head != None):
            node.prev = self.head
        self.head = node

        if (self.min == None or self.min.data > data):
            node = self.Node(data)
            node.prev = self.min
            self.min = node

    def pop(self):
        data = None
        if (self.head != None):
            data = self.head.data
            self.head = self.head.prev

        if (self.min != None and self.min.data == data):
            self.min = self.min.prev
        return data

    def get_min(self):
        if self.min != None:
            return self.min.data
        return None

def test():
    s = Stack()

    for i in range(9, -1, -1):
        s.push(i)
        print(s.get_min() == i)

    for i in range(10):
        print(s.get_min() == i)
        s.pop()
test()