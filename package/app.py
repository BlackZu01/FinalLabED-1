import numpy as np
from classes import LinkedList

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