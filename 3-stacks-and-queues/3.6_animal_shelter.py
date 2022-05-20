# Cracking the code interview 
#
# 3.6 - Animal Shelter
# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out"
# basis. people must adopt either the "oldest" (based on arrrival time) of all animals at the shelter,
# or they can select wether they could preffer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data sctructures to
# maintain this system and implements operation such as enqueue, dequeueAny, dequeueDog and dequeueCat.
# You may use the built-in LinkedList data structure.

import gc

class Queue:

    class Node:
        def __init__(self, data = None):
            self.data = data # Dog or Cat
            self.next = None

    def __init__(self):
        self.first = None

    def isEmpty(self):
        return (self.first == None)

    def peek(self):
        return self.first

    def remove(self):
        if self.isEmpty():
            return None
        pivot = self.first
        self.first = self.first.next
        data = pivot.data
        del(pivot)
        gc.collect()
        return data

    def add(self, data):
        node = self.Node(data)
        
        if self.first == None:
            self.first = node
        else:
            pivot = self.first
            while pivot.next != None:
                pivot = pivot.next
            pivot.next = node

    def dequeueAny(self):
        return self.remove()

    def enqueue(self, data):
        return self.add(data)    

    def is_cat_or_dog(self, data):
        if data.startswith("Dog"):
           return "Dog"
        elif data.startswith("Cat"):
           return "Cat"
        else:
            return None

    def dequeue(self, type=None):
        if type == None:
            return self.dequeueAny()
        elif self.is_cat_or_dog(type) != None:
            pivot = self.first
            prev = pivot
            while pivot.next != None and self.is_cat_or_dog(pivot.data) != type:
                prev = pivot
                pivot = pivot.next

            if prev != pivot and pivot != None and pivot.data.startswith(type):
                prev.next = pivot.next
            else:
                self.first = pivot.next
            data = pivot.data
            del(pivot)
            gc.collect()
            return data
        else:
            return ""

    def dequeueCat(self):
        return self.dequeue(type="Cat")
    
    def dequeueDog(self):
        return self.dequeue(type="Dog")

    def __str__(self):
        res = ""
        pivot = self.first
        while pivot != None and pivot.next != None:
            res += f"{pivot.data} "
            pivot = pivot.next
        return res

def test():
    q = Queue()
    for i in range(20):
        if i % 2 == 0:
            q.add(f"Dog-{i}")
        else:
            q.add(f"Cat-{i}")

    print(q)
    for i in range(10):
        print(q.dequeueCat()).startswith("Cat"))
    for i in range(10):
        print(q.dequeueDog()).startswith("Dog"))


test()