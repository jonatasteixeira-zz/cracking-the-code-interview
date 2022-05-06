# Cracking the code interview 
#
# 2.6 - Palindrome
# Implement a function to check if a list is a palindrome

class Node():
    def __init__(self, value = None):
        self.value = value
        self.n_next = None
        self.n_prev = None

    def is_palindrome(self):
        start = self.get_first()
        end = self.get_last()

        while (start != end and (start.n_next != end or end.n_prev != start)):
            if (start.value != end.value):
                return False
            start = start.n_next
            end = end.n_prev

        return True

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
    a = Node(0)
    a.append(1); a.append(2); a.append(3); a.append(2); a.append(1); a.append(0)

    print(a.is_palindrome() == True)

    a = Node(0)
    a.append(1); a.append(2); a.append(3); a.append(3); a.append(1); a.append(0)
    print(a.is_palindrome() == False)

test()