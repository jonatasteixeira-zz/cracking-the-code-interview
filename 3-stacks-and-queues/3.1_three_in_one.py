# Cracking the code interview 
#
# 3.1 - Three in one
# Describge how you could use a single array to implement a stack

class Stack:
    def __init__(self):
        self.head = 0
        self.MAX_SIZE = 10
        self.stack = [None] * self.MAX_SIZE

    def pop(self):
        if self.head > 0:
            self.head = self.head - 1 
            node = self.stack[self.head]
            self.stack[self.head] = None 
            return node
    
    def push(self, item):
        if self.head >= self.MAX_SIZE:
            self.MAX_SIZE *= 2
            self.stack += [None] * self.MAX_SIZE
        self.stack[self.head] = item
        self.head += 1

    def peek(self):
        if self.head > 0:
            return self.stack[self.head - 1]
    
    def isEmpty(self):
        return (self.head == 0)

def test():
    s = Stack()
    for i in range(100):
        s.push(i)
    
    print (s.peek())
    print (s.peek())

    for i in range(100):
        print(s.pop() == (99-i))

    print(s.isEmpty())

test()