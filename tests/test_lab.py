from package.classes import LinkedList
from package.classes import Stack

def test_add_node():
    lista = LinkedList()
    lista.add_node(5)
    
    print(lista)
    assert lista.values == [5]

def test_add_node_stack():
    stack = Stack()
    stack.addNode(73)
    stack.addNode(37)

    assert stack.values == [37, 73]