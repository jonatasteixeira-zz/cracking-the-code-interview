# Cracking the code interview 
#
# 2.7 - Intersection
# Given two (singly) linked lists, determine if the two lists intersect. Return the intersection node, 
# Note that the intersection is defined based on reference, not value. That i, if the kth node
# of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting

def intersection(a, b):
    head_a = a.get_first()
    while (head_a.n_next != None):
        head_b = b.get_first()
        while (head_b.n_next != None):
            if (head_b == head_a):
                return head_a.value
            head_b = head_b.n_next
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
        else:
            last = self.get_last()
            node = Node(value)
            node.n_prev = last
            last.n_next = node

def test():
    a = Node('a')
    a.append('a'); a.append('a'); a.append('a'); 
    b = Node('b')
    b.append('b'); b.append('b'); b.append('b'); 
    c = Node(0)
    c.append(1); c.append(1); c.append(1);

    a.get_last().n_next = c
    b.get_last().n_next = c
    
    print(a)
    print(b)
    print(c)

    print(intersection(a, b))

test()