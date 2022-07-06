# Cracking the code interview 
#
# 4.3 - List of dephts
# Given a binary tree, create a linked list of all the nodes at each depth. 
# If you have a tree with depth D, create D linked lists

class Node:
    def __init__(self, val):
        self.val =  val
        self.right = self.left = None

    def add(self, val):
        root = self.search(val)
        node = Node(val)
        if node.val > root.val:
            temp = root.right
            root.right = node
            node.right = temp
        else:
            temp = root.left
            root.left = node
            node.left = temp

    def check_bst(self):
        def check_bst_aux(node):
            if node == None:
                return True

            if (node.right and node.right.val < node.val) and (node.left and node.left.val > node.val):
                return False
               
            return check_bst_aux(node.left) and check_bst_aux(node.right)
        return check_bst_aux(self)


    def search(self, val):
        prev = None
        root = self
        while root != None:
            if val == root.val:
                return root
            elif val > root.val:
                prev = root
                root = root.right
            else:
                prev = root
                root = root.left
        return prev

    def list_of_depths(self):
        list1 = [self]
        list2 = []
        
        list_index = 0
        def print_val(list):
            print(f"List Depth {list_index}: {[ node.val for node in list]}")

        while list1: # len(list1) != 0:
            print_val(list1)
            list_index += 1
            for node in list1:
                if node.left != None:
                    list2.append(node.left)
                if node.right != None:
                    list2.append(node.right)
            list1 = list2
            list2 = []


    def __str__(self):
        def aux(node):
            if node == None:
                return "*"
            res = f"{node.val}: [{aux(node.left)} {aux(node.right)}] "
            return res
        return aux(self)

def test():
    import random

    node = Node(8)
    for i in range(20):
        node.add(random.randint(0, 20))
    print(node)

    node.list_of_depths()

    print(node.check_bst())

test()