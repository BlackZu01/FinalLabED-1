from __future__ import annotations
from .node import Node

class NodeCol(Node):
    def __init__(self, data=None) -> None:
        super().__init__(data)
        self.nextCol = Stack()

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