# Clases para la resolucion del problema

class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> None:
        return str(self.data)

class NodeCol(Node):
    def __init__(self, data=None) -> None:
        super().__init__(data)
        self.nextCol = Stack()

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

class Stack:
    def __init__(self, values=None) -> None:
        self.head = values
        self.tail = values 
        if values != None:
            ...
    
    def __iter__(self):
        current = self.head 
        while current:
            yield current
            current = current.next 

    def __str__(self):
        return ' -> '.join([str(node) for node in self])

    def add_node_list(self, value: int) -> None:
        node = NodeCol(value)

        if self.head == None:
            self.head = node
            self.tail = node
            self.tail.next = None
            return
        self.tail.next = node
        self.tail = self.tail.next

    def addNodeStack(self, value=None):
        P = NodeCol(value)
        if self.head == None:
            self.head = P 
            self.tail = P 
            self.tail.next = None 
            return 
        P.next = self.head 
        self.head = P

    @property 
    def values(self):
        return [node.data for node in self]