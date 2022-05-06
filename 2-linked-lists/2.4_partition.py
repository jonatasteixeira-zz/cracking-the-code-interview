# Cracking the code interview 
#
# 2.4 - Partition
# Write code to partition a linked list around value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the value of x only need
# ot be after the elements less than x (see below) The partition element x can appear anywhere in the 
# "right partition"; it does not to appear between the left and right partitions. 
#
# EXAMPLE
# input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition 5]
# output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 

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

    def partition(self, value):
        minor = Node()
        major = Node()
        head = self.get_first()

        while (head != None):
            if head.value < value:
                minor.append(head.value)
            else:
                major.append(head.value)
            new_head = head.n_next
            del(head)
            head = new_head

        minor = minor.get_last()
        major = major.get_first()
        minor.n_next = major
        major.n_prev = minor
        return minor.get_first()

def test():
    a = Node(3)
    a.append(5); a.append(8); a.append(5); a.append(10); a.append(2); a.append(1)
    print(a)
    print(a.partition(5))

test()