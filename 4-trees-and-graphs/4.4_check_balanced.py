# Cracking the code interview 
#
# 4.4 - Check balanced
# Check if a binary tree is balanced. For the purposes of this question, a balanced tree 
# is a tree such that the heights of the two subtrees of any node never differ by more than one.

class Node:
    def __init__(self, val):
        self.val = val
        self.right = self.left = None

    def add(self, val):
        root = self.search(val)
        node = Node(val)

        if val > root.val:
            temp = root.right
            root.right = node
            node.right = temp
        else:
            temp = root.left
            root.left = node
            node.left = temp
    
    def search(self, val):
        prev = None
        root = self
        while root != None:
            if val == root:
                return root
            elif val > root.val:
                prev = root
                root = root.right
            else:
                prev = root
                root = root.left
        return prev
    
    def is_balanced(self):
        def height(node):
            if node == None:
                return 0
            
            left = height(node.left)
            if left == -1:
                return -1
            
            right = height(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        return (height(self) != -1)


    def __str__(self):
        def aux(node):
            if node == None:
                return "*"
            return f"{node.val}: [{aux(node.left)} {aux(node.right)}] "
        return aux(self)

def test():
    import random

    node = Node(8)
    for i in range(20):
        node.add(random.randint(0, 20))
    print(node)

    print()

test()



