# Cracking the code interview 
#
# 2.2 - Return kth to last
# Implement an algorithm to find the Kth to last element of a singly linked list

# Class to specify a linked list
class Node:
    def __init__(self, data):
        self.next = None
        self.data = None

    # private
    def _get_last_(self):
        pivot = self
        while (pivot.next != None):
            pivot = pivot.next
        return pivot

    # If no data, return the size of list
    def index_of(self, data=None):
        pivot = self
        index = 0
        while (pivot != None):
            if ( (data != None) and (pivot.data == data) ):
                return index
            pivot = pivot.next
            index +=1

        if (data == None):
            return index
        else:
            return -1

    def append(self, data):
        node = Node(data)
        last = self._get_last_()
        last.next = node

    def get_size(self):
        return self.index_of()


def test():
    n = Node(1)
    n.append(2)
    print(n.get_size() == 2)
    n.append(3)
    print(n.get_size() == 3)

test()
