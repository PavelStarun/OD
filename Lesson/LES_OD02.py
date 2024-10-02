
# Стек (Stack) — это структура данных, работающая по принципу "последний пришел, первый ушел" (Last In, First Out,
# LIFO).


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())


#######################################################################

# ✅ Очередь (Queue) — это структура данных, работающая по принципу "первый пришел — первый ушел" (First In, First Out).

class Queue:
    def __init__(self):
        self.items = []


def is_empty2(self):
    return self.items == []


def enqueue(self, item):
    self.items.insert(0, item)


def dequeue(self):
    return self.items.pop()


# [1]
# [2, 1]
# [3, 2, 1]
# [4, 3, 2, 1]
# [5, 4, 3, 2, 1]
def size(self):
    return len(self.items)


queue = Queue()

print(queue.is_empty2())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# ["действие 4", "действие 3", "действие 2", "действие 1"]

print(queue.is_empty2())
print(queue.size())
print(queue.dequeue())
print(queue.size())

#######################################################################


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        # {0: [1, 4], 1: [2, 3, 4], 2: [3], 3: [4]}
        for node in self.graph:
            print(node, "->", " -> ".join(map(str, self.graph[node])))


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_graph()


#####################################################################


class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

        # Функция для добавления нового узла


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


root = Node(70)

root = insert(root, 30)
root = insert(root, 56)
root = insert(root, 89)
root = insert(root, 45)
root = insert(root, 60)
root = insert(root, 73)
root = insert(root, 98)
root = insert(root, 84)


###################################################################

