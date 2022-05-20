# Cracking the code interview 
#
# 3.5 - Sort Stack
# Write a program to sort a stack such that the smallest items are on the top. You can use
# ona ddictional temporary stack, but you may not copy the elements into any other data structure
# (such as an arrary). The stack supports the following operations: push, pop, peek and isEmpty.

import gc

from pyparsing import opAssoc


class Stack:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.prev = None
        
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return (self.head == None)

    def push(self, data):
        node = self.Node(data)
        node.prev = self.head
        self.head = node

    def pop(self):
        if self.isEmpty():
            return None

        node = self.head
        self.head = self.head.prev
        data = node.data
        del(node)
        gc.collect()
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data

    def __str__(self):
        node = self.head
        res = ""
        while (node != None):
            res += f"{node.data} "
            node = node.prev
        return res

    def sort(self):
        aux = Stack()

        while not self.isEmpty():
            bigger = self.pop()
            buffer = 0

            while not aux.isEmpty() and bigger > aux.peek():
                data = aux.pop()
                self.push(data)
                buffer += 1
            aux.push(bigger)

            while buffer > 0:
                data = self.pop()
                aux.push(data)
                buffer -= 1

        head = aux.head
        aux.head = self.head
        self.head = head

def test():

    s = Stack()
    import random
    for i in range(20):
        s.push(random.randint(0, 100))

    print(s)
    s.sort()
    print(s)

    last = s.peek()
    for i in range(20):
        print(s.peek() >= last)
        last = s.pop()

test()


