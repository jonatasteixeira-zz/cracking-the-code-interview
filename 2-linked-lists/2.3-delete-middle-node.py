# Cracking the code interview 
#
# 2.3 - Delete middle node
# Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # Private
    def _get_last_(self):
        last = self
        while (last.next != None):
            last = last.next
        return last

    def append(self, data):
        node = Node(data)
        last = self._get_last_()
        last.next = node

    def remove(self, data):
        pivot = self
        if (pivot.data == data): # Should remove first element
            pivot.data = None
            if (pivot.next != None): # 
                pivot.data = pivot.next.data
                pivot.next = pivot.next.next
        else:
            while (pivot.next != None):
                if (pivot.next.data == data):
                    pivot.next = pivot.next.next
                    return
                pivot = pivot.next

    def to_s(self):
        pivot = self
        string = ""
        while (pivot != None):
            string += str(pivot.data)
            pivot = pivot.next
        return string

def test_remove():
    n = Node(1)
    n.append(2)
    n.append(3)
    n.append(4)
    print(n.to_s() == "1234")

    n.remove(4)
    print(n.to_s() == "123")

    n.remove(2)
    print(n.to_s() == "13")

    n.remove(1)
    print(n.to_s() == "3")

    n.remove(3)
    print(n.to_s() == "None")

test_remove()
