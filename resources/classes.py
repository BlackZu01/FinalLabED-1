# Clases para la resolucion del problema
import numpy as np
class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> None:
        return str(self.data)

class NodeCol(Node):
    def __init__(self, data=None) -> None:
        super().__init__(data)

class NodeRow(Node):
    def __init__(self, data=None) -> None:
        super().__init__(data)
        self.nextRow = LinkedList()

class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None

        if values is not None:
            ...

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next
    
    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    @property
    def values(self):
        return [node.data for node in self]

    def add_node(self, value: int) -> None:
        node = NodeRow(value)

        if self.head == None:
            self.head = node
            self.tail = node
            self.tail.next = None
            return
        self.tail.next = node
        self.tail = self.tail.next

class ColumnList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None

        if values is not None:
            ...

    def __iter__(self):
        current = self.head

        while current:
            yield current
            current = current.next

    def __str__(self):
        return ' -> '.join([str(node) for node in self])
        
    def add_node(self, value=None):
        node = NodeCol(value)

        if self.head == None:
            self.head = node
            self.tail = node
            self.tail.next = None
            return
        self.tail.next = node
        self.tail = self.tail.next

    @property
    def values(self):
        return [node.data for node in self]
    
matrix = np.zeros((3, 3), dtype=int)

k=0
for i in range(3):
    for j in range(3):
        matrix[i][j] = k
        k += 1

lista = LinkedList()

for i in range(matrix.shape[1]):
    lista.add_node(matrix[0][i])

p = lista.head
for j in range(matrix.shape[0]):
    p.nextRow.add_node(matrix[1][j])

p1 = p.nextRow.head
for j in range(matrix.shape[0]):
    p1.nextRow.add_node(matrix[2][j])

def printMat(Matrix):
    for i in range(Matrix.shape[0]):
        for k in range(Matrix.shape[1]):
            print(Matrix[i][k], end=' ')
        print(' ')
    
print('La matriz es ')
printMat(matrix)

print('\nY la lista: ')
print(lista)
print(lista.head.nextRow)
print(lista.head.nextRow.head.nextRow)

