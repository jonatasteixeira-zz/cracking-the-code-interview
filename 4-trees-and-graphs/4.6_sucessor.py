# Cracking the code interview 
#
# 4.5 - Sucessor
# Write an algorithm to find the "next" node (i.e., in-order sucessor) of a given node in a
# binary search tree. You can assume each node as a link to its parent


class Node:
    def __init__(self, data=None):
        self.parent, self.right, self.left = None, None, None
        self.data = data

    def insert(self, data):
        root = self.search(data)
        node = Node(data)
        node.parent = root

        if data > root.data:
           temp = root.right
           root.right = node
           node.left = temp
        else:
            temp = root.left
            root.left = node
            node.right = temp

    def most_left(self, node):
        while (node):
            pivot = node
            node = node.left
        return pivot

    def most_right(self, node):
        while (node):
            pivot = node
            node = node.right
        return pivot

    def next_node(self, node):
        if node.right:
            return self.most_left(node.right)
        if node.parent:
            return self.most_left(node.parent.right)
        return None


    def search(self, data):
        def aux_search(parent, node, data):
            if node == None:
                return parent
            if node.data == data:
                return node

            if data > node.data:
                return aux_search(node, node.right, data)
            else:
                return aux_search(node, node.left, data)    

        return aux_search(None, self, data)

    def list_of_depths(self):
        list1 = [self]
        list2 = []
        
        list_index = 0
        spaces = 32
        def print_data(list, spaces = 32):
            string = f"List Depth {list_index}: "
            for node in list:
                string += f"{' ' * spaces}{node.data}{' ' * spaces}"
            print(string)
            

        while list1: # len(list1) != 0:
            print_data(list1, spaces)
            list_index += 1
            spaces = spaces // 2
            for node in list1:
                if node.left != None:
                    list2.append(node.left)
                if node.right != None:
                    list2.append(node.right)
            list1 = list2
            list2 = []


    def __str__(self):
        def preorder(node):
            if node == None:
                return "*"
            return f"{node.data} [{preorder(node.left)} {preorder(node.right)}] "

        def inorder(node):
            if node == None:
                return "*"
            return f"[{inorder(node.left)} {node.data} {inorder(node.right)}] "

        def postorder(node):
            if node == None:
                return "*"
            return f"[{postorder(node.left)} {postorder(node.right)}] {node.data}"


        res = f"{preorder(self)}\n"
        res += f"{inorder(self)}\n"
        res += f"{postorder(self)}\n"
        return res


def test():
    import random

    node = Node(4)
    for i in range(10):
        node.insert(random.randint(0, 20))
    


    print(node)

    node.list_of_depths()
    print(node.next_node(node).data)

test()