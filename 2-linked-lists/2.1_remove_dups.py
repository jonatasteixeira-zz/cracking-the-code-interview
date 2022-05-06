# Cracking the code interview 
#
# 2.1 - Remove Dups
# Write a code to remove duplicates from a unsorted linked list
# How would you solve this problem if a temporary buffer is not allowed

# Class to specify a linked list
class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

    # Private
    def _get_first_(self):
        first = self
        while (first.prev != None):
            first = first.prev
        return first

    # Private
    def _get_last_(self):
        last = self
        while (last.next != None):
            last = last.next
        return last

    # Private
    def _remove_all_after_(self, node, data):
        while (node != None):
            if (node.data == data):
                self.remove(node)
            node = node.next

    def append(self, data):
        last = self._get_last_()
        node = Node(data)
        node.prev = last
        last.next = node
        return node

    def remove(self, node):
        if (node.prev != None):
            node.prev.next = node.next
        if (node.next != None):
            node.next.prev = node.prev
        del node

    # O(N2) time
    def remove_duplicates(self):
        pivot = self._get_first_()
        while (pivot != None):
            self._remove_all_after_(pivot.next, pivot.data) # It will remove all accours of data in the rest of the list
            pivot = pivot.next
    
    def print_all(self):
        pivot = self._get_first_()
        while (pivot.next != None):
            print(pivot.data),
            pivot = pivot.next
        print(pivot.data)


def test_remove_duplicates():
    l = Node(1)
    l.append(2)
    l.append(3)
    l.append(2)
    l.append(2)
    l.append(3)
    l.remove_duplicates()
    l.print_all()

test_remove_duplicates()