# Cracking the code interview 
#
# 2.8 - Loop detection
# Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# 
# DEFINITION
# Cirrcular linked list: A (corrupt) linked list wich a nodes's next pointer points to an earlier node, so
# as to make a loop in the linked list.
#
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the samne C as earlier]
# output: C

def loop_detection(a):
    refs = []
    head_a = a.get_first()
    while (head_a != None):
        print(refs)
        if head_a in refs:
            return head_a
        refs.append(head_a)
        head_a = head_a.n_next

class Node():
    def __init__(self, value = None):
        self.value = value
        self.n_next = None
        self.n_prev = None

    def get_first(self):
        node = self
        while (node.n_prev != None):
            node = node.n_prev
        return node

    def get_last(self):
        node = self
        while (node.n_next != None):
            node = node.n_next
        return node

    def __str__(self):
        node = self.get_first()
        string = '[ ' + str(node.value)
        while node.n_next != None:
            node = node.n_next
            string += ', ' + str(node.value)
        string += ']'
        return string

    def append(self, value):
        if self.value == None:
            self.value = value
            return self
        else:
            last = self.get_last()
            node = Node(value)
            node.n_prev = last
            last.n_next = node
            return node

def test():
    a = Node(0)
    a.append(1); a.append(2); a.append(3); 
    loop = a.append(4)
    a.append(5); a.append(6); a.append(7)
    a.get_last().n_next = loop
    
    a = loop_detection(a)
    print(a.value)

test()