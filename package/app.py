import numpy as np
from classes import LinkedList
from classes import Stack

matrix = np.zeros((3, 3), dtype=int)

k=0
for i in range(3):
    for j in range(3):
        matrix[i][j] = k
        k += 1

lista = LinkedList()

# Añadimos la primera fila
for i in range(matrix.shape[1]):
    lista.add_node(matrix[0][i])

# Añadimos el resto
p = lista.head
for k in range(1, matrix.shape[0]):
    for j in range(matrix.shape[0]):
        p.nextRow.add_node(matrix[k][j])
    p = p.nextRow.head

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

# Stack  para la multiplicacion

matrix_stack = np.zeros((3, 3), dtype=int)
stack = Stack()

k=0
for i in range(3):
    for j in range(3):
        matrix_stack[i][j] = k+1
        k += 1

for i in range(matrix_stack.shape[1]):
    stack.add_node_list(matrix_stack[0][i])

p = stack.head
for k in range(matrix_stack.shape[0]):
    for j in range(matrix_stack.shape[1]):
        p.nextCol.addNodeStack(matrix_stack[j][k])
    p = p.nextCol.head

print('La matriz es ')
printMat(matrix_stack)

print('\nY la lista: ')
print(stack.head.nextCol)

print(stack.head.nextCol.head.nextCol)
print(stack.head.nextCol.head.nextCol.head.nextCol)