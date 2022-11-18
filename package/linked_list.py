from __future__ import annotations
from .node import Node

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