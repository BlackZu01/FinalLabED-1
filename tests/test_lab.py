from resources.classes import LinkedList

def test_add_node():
    lista = LinkedList()
    lista.add_node(5)
    
    print(lista)
    assert lista.values == [5]