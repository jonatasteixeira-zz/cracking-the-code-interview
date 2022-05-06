# Cracking the code interview 
#
# 3.3 - Stack of Plates
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. There-
# fore, in real life, we would likely start a new stack when the previous stack exceeds
# some threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
# Stacks should be composed of several stacks, and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
# behave identically to a single stack (that is, pop() should return the same values as it
# would if there were just a single stack).

class Stack:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.prev = None

    def __init__(self, data=None):
        self.size = 0 

        if (data == None):
            self.head = None
        else:
            self.head = self.Node(data)
            self.size += 1
        self.prev = None

    def pop(self):
        data = self.head.data
        tmp = self.head
        self.head = self.head.prev
        self.size -= 1
        del (tmp)
        return data

    def push(self, data):
        node = self.Node(data)
        node.prev = self.head
        self.head = node
        self.size += 1


class SetOfStack:
    LIMIT = 3
    stacks = []

    def __init__(self):
        self.stacks=[Stack()]
        self.LIMIT = 3

    def get_current_stack(self):
        if (len(self.stacks) > 0):
            return self.stacks[len(self.stacks)-1]
        return None

    def push(self, data):
        current_stack = self.get_current_stack()

        if (current_stack.size == self.LIMIT):
            self.stacks.append(Stack(data))
        else:
            current_stack.push(data)

    def pop(self):
        current_stack = self.get_current_stack()

        if (current_stack != None and current_stack.size <= 0):
            self.stacks.remove(current_stack)
            current_stack = self.get_current_stack()

        if (current_stack != None):
            data = current_stack.pop()
            return data
        return None

def test():
    s = SetOfStack()
    for i in range(20):
        s.push(i)

    for i in range(19, -1, -1):
        print(s.pop() == i)
    print(s.pop() == None)

        
test()