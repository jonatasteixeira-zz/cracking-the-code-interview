

def sum_lists(list_a, list_b):
    result = Node()
    pivot_a = list_a.get_last()
    pivot_b = list_b.get_last()

    go_one = 0

    while (pivot_a != None and pivot_b != None):
        tmp_sum = (pivot_a.value + pivot_b.value + go_one) 
        if (tmp_sum > 10):
            tmp_sum = tmp_sum - 10
            go_one = 1
        else:
            go_one = 0    
        result.append(tmp_sum)
        pivot_a = pivot_a.n_prev
        pivot_b = pivot_b.n_prev

    return result

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
    a = Node(1)
    a.append(2)
    a.append(3)

    b = Node(3)
    b.append(2)
    b.append(1)

    print(sum_lists(a, b))

test()