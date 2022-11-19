from .stack import Stack
from .linked_list import LinkedList

class Prod:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None 

    def compute(self, lista_uno: LinkedList, lista_dos: Stack):
        self.lista_uno = lista_uno
        self.lista_dos = lista_dos
        value = 0

        current = self.lista_uno.head 
        current2 = self.lista_dos.head.nextCol.head
        temp1, temp2 = (current, current2)

        while current and current2:
            ...