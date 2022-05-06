# Cracking the code interview 
#
# 3.4 - Queue via Stacks
# Implement a MyQueue class which implements a queue using two stacks.

import gc

class Stack:
    
    class Node:
        def __init__(self):
            self.data = None
            self.prev = None
    
    def __init__(self):
        self.head = None

    def push(self, data):
        node = self.Node()
        node.data = data
        node.prev = self.head
        self.head = node

    def pop(self):
        if (self.head == None):
            return None
        node = self.head
        self.head = self.head.prev
        data = node.data
        del(node)
        gc.collect()
        return data


class MyQueue:

    def __init__(self):
        self.stacks = [Stack(), Stack()] 
        self.current = 0
        self.should_invert = 0 # False

    def stack(self):
        return self.stacks[self.current]

    def add(self, data):
        self.stack().push(data)
        self.should_invert = 1 # True

    def remove(self):
        if (self.should_invert == 1):
            self.should_invert = 1 - self.should_invert # Toogle 1 and 0
            new_current = 1 - self.current 

            data = self.stack().pop() 
            while (data != None):
                self.stacks[new_current].push(data)
                data = self.stack().pop()
            self.current = new_current   

        data = self.stack().pop() 
        return data

def test():
    queue = MyQueue()

    for _ in range(5):
        for i in range(10):
            queue.add(i)

        for i in range(10):
            print(queue.remove() == i)

test()
