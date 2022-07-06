# Cracking the code interview 
#
# 4.2 - Minimal tree
# Given a sorted (increasing order) array with unique integer elements, write 
# an algorithm to create a binary search tree with minimal height

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.left = None
        self.heigh = 0

    def add(self, val):
        root = self.search(val)
        node = Node(val)

        if root != None:
            if val > root.val:
                temp = root.right
                root.right = node
                node.right = temp
            else:
                temp = root.left
                root.left = node
                node.left = temp

        return node

    def check_bst(self):
        def check_bst_aux(node):
            if node == None:
                return True

            if (node.right and node.right.val < node.val) and (node.left and node.left.val > node.val):
                return False
               
            return check_bst_aux(node.left) and check_bst_aux(node.right)
        return check_bst_aux(self)

    def add_array(self, array):
        for val in array:
            self.add(val)

    def search(self, val):
        def search_aux(node, val, father=None):
            if node == None:
                return father
            if node.val == val:
                return node
            
            if val > node.val:
                return search_aux(node.right, val, node)
            else:
                return search_aux(node.left, val, node)

        return search_aux(self, val)

    def __str__(self):
        def aux(node):
            if node == None:
                return "*"
            return f"{node.val}: [{aux(node.left)} {aux(node.right)}] "
        return aux(self)


def test():

    node = Node(8)
    node.add_array([1,2,3,4,5,6,7,8,9,10,11,12,131,14,15,16])

    print(node)
    print(node.check_bst())

test()