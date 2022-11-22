import numpy as np
from scipy.linalg import lu

class Node:
    def __init__(self, value: list, next_node=None, prev_node=None) -> None:
        self.valor = value[0]
        self.i = value[1]
        self.j = value[2]
        self.n = value[3]
        self.m = value[4]
        self.next = next_node
        self.prev = prev_node

    def __str__(self) -> str:
        return "║ X: "+ str(self.valor) +", (i,j): ("+ str(self.i) + ","+ str(self.j) +") ║"


class LinkedList:
    def __init__(self, values=None) -> None:
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple_nodes(values)
            
    def __str__(self) -> str:
        return ' --> '.join([str(node) for node in self])
    
    def __len__(self) -> int:
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
    
    def __iter__(self) -> None:
        current = self.head
        while current:
            yield current
            current = current.next
            
    @property
    def values(self) -> list:
        return [[node.valor,node.i,node.j ] for node in self]
    
    def add_node(self, value:list):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values: list):
        for value in values:
            self.add_node(value)
    
    def deletenode(self, node: Node):
        p = node
        current = self.head 
        prev = None 

        while current != None and current != node:
            prev = current 
            current = current.next

        if node == self.head:
            self.head = current.next
        elif node == self.tail:
            self.tail = prev 
            prev.next = None 
        else:
            prev.next = current.next
            current.next = None
    
    def Mat_to_list(self, Mat) -> None:
        value = []
        for i in range(Mat.shape[0]):
            for j in range(Mat.shape[1]):
                if(Mat[i][j] != 0):
                    value.append([Mat[i][j], i, j, Mat.shape[0],Mat.shape[1]]) 
        self.add_multiple_nodes(value)

    def List_to_Mat(self) -> np.array:
        New_Mat = np.zeros([self.head.n,self.head.m])
        for node in self:
            if(New_Mat[node.i][node.j] != 0 ):
                New_Mat[node.i][node.j] += node.valor
            else:
                New_Mat[node.i][node.j] = node.valor
        return New_Mat

def additionLinkedList(Mat1: LinkedList(), Mat2: LinkedList()) -> LinkedList():
    if(Mat1.head.n == Mat2.head.n and Mat1.head.m == Mat2.head.m):
        result_matrix = LinkedList()
        for node1 in Mat1:
            sw = 0
            for node2 in Mat2:
                sw2 = 0
                if(node1.i == node2.i and node1.j == node2.j):
                    sw = 1
                    Value = [node1.valor + node2.valor,node1.i,node1.j, node1.n, node1.m]
                    result_matrix.add_node(Value)
            if(sw != 1):
                Value = [node1.valor,node1.i,node1.j, node1.n, node1.m]
                result_matrix.add_node(Value)
        for node2 in Mat2:
            sw = 0
            for node1 in Mat1:
                if(node1.i == node2.i and node1.j == node2.j):
                    sw = 1
            if(sw != 1):
                Value = [node2.valor,node2.i,node2.j, node1.n, node1.m]
                result_matrix.add_node(Value)
        return result_matrix
    else:
        print("Las dimensiones no coinciden")

def subtractLinkedList(Mat1: LinkedList(), Mat2: LinkedList()) -> LinkedList():
    if(Mat1.head.n == Mat2.head.n and Mat1.head.m == Mat2.head.m):
        result_matrix = LinkedList()
        for node1 in Mat1:
            sw = 0
            for node2 in Mat2:
                sw2 = 0
                if(node1.i == node2.i and node1.j == node2.j):
                    sw = 1
                    Value = [node1.valor - node2.valor,node1.i,node1.j, node1.n, node1.m]
                    result_matrix.add_node(Value)
            if(sw != 1):
                Value = [node1.valor,node1.i,node1.j, node1.n, node1.m]
                result_matrix.add_node(Value)
        for node2 in Mat2:
            sw = 0
            for node1 in Mat1:
                if(node1.i == node2.i and node1.j == node2.j):
                    sw = 1
            if(sw != 1):
                Value = [-node2.valor,node2.i,node2.j, node1.n, node1.m]
                result_matrix.add_node(Value)
        return result_matrix
    else:
        print("Las dimensiones no coinciden")

def multiply(Mat1: LinkedList(), Mat2: LinkedList()) -> LinkedList():
    if(Mat1.head.m == Mat2.head.n):
        result_matrix = LinkedList()
        for node2 in Mat2:
            for node1 in Mat1:
                if(node2.i == node1.j):
                    result_matrix.add_node([node1.valor * node2.valor,node1.i,node2.j, node1.n, node2.m])
        return result_matrix

def Determinat(Mat1: LinkedList()) -> int:
    if(Mat1.head.n == Mat1.head.m):
        P, L, U = lu(Mat1.List_to_Mat())
        nswaps = len(np.diag(P)) - np.sum(np.diag(P)) - 1
        detP = (-1)**nswaps
    
        aux1 =LinkedList()
        aux2 =LinkedList()
        aux1.Mat_to_list(U)
        aux2.Mat_to_list(L)
        det = 1
        for node1 in aux1:
            if (node1.i == node1.j):
                det *= node1.valor
                if np.prod(np.diag(U)) == 0:
                    det = 0 
        for node2 in aux2:
            if (node2.i == node2.j):
                det *= node2.valor
                if np.prod(np.diag(L)) == 0:
                    det = 0 
        det = det * detP
        if(np.linalg.det(Mat1.List_to_Mat()) > 0):
            det = np.abs(det)
        else:
            det = np.abs(det) * -1
            
        return round(det)
    else:
        return 'La matrix no es nxn'

def multiplywithn(Mat1: LinkedList(), n: int) -> LinkedList():
    for node1 in Mat1:
        node1.valor = node1.valor * n
    return Mat1