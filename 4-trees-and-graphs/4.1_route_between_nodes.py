# Cracking the code interview 
#
# 4.1 - Routes between nodes
# Given a directed graph, design an algorithm to find out whether there is a
# rote between two nodes.

from collections import defaultdict
import gc


class Graph():
    def __init__(self, directional=False):
        self.graph = {}
        self.directional = directional

    def add_node(self, node):
        if node == None:
            return False
        self.graph[node] = set()
        return self.graph[node]

    def add_connection(self, node1, node2):
        if node1 not in self.graph or node2 not in self.graph:
            return False
        self.graph[node1].add(node2)
        if not self.directional:
            self.graph[node2].add(node1)
        return True

    def dfs(self, node, goal):
        if node == None:
            return False

        stack  = [node]
        visited = {}

        while len(stack) > 0:
            node = stack.pop()
            visited[node] = True
            if node == goal:
                return node
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return False

    def bfs(self, node, goal):
        if node == None:
            return False

        queue  = [node]
        visited = {}

        while len(queue) > 0:
            node = queue.pop(0)
            visited[node] = True
            if node == goal:
                return node
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False


    def minimum_path(self, node1, node2):
        distances = {node: [None, 999999] for node in range(len(self.graph))}

        visited = []    
        to_visit = [node1]

        distances[node1] = [None, 0]

        while to_visit:
            pivot = None
            for node in to_visit:
                if pivot == None or distances[node][1] < distances[pivot][1]:
                    pivot = node
            to_visit.remove(pivot)

            if pivot == node2:
                path = f"{pivot} "
                while distances[pivot][0] != None:
                    pivot = distances[pivot][0]
                    path = f"{pivot} {path}"
                return path

            for node in self.graph[pivot]:
                if node not in visited:
                    to_visit.append(node)
                    if distances[node][1] > distances[pivot][1] + 1:
                        distances[node][0] = pivot
                        distances[node][1] = distances[pivot][1] + 1

            visited.append(pivot)

    def has_path(self, node1, node2):
        #return self.dfs(node1, node2)
        return self.bfs(node1, node2)

    def __str__(self):
        res = ""
        for node in self.graph:
            res += f"{node}: ("
            for edge in self.graph[node]:
                res += f"{edge}, "
            res += ")\n"
        return res



def test():
    import random

    g = Graph(directional=True)   
    for i in range(20):
        g.add_node(i)
    for i in range(40):
        g.add_connection(random.randint(0, 20), random.randint(0,20))

    print(g)

    if (g.has_path(0, 19)):
        print(g.minimum_path(0, 19))
    else:
        print("There is no way between 0 e 19")

test()