from .linked_list import LinkedList

class Addition:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None

    def compute(self, lista_uno: LinkedList, lista_dos: LinkedList):
        self.lista_uno = lista_uno
        self.lista_dos = lista_dos 

        current = self.lista_uno.head
        current2 = self.lista_dos.head
        while current:
            if self.head == None:
                self.head = current + current2     
            current = current.next
            current = current2.next

            if current == None:
                current = self.lista_uno.head.nextRow.head
                current2 = self.lista_dos.head.nextRow.head