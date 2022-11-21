from Listas import LinkedList, additionLinkedList, Determinat, subtractLinkedList, multiply
import numpy as np

Mat1 =np.loadtxt('Matrixs\Mat5.txt')
Mat2 =np.loadtxt('Matrixs\Mat5.txt')
list1 = LinkedList()
list2 = LinkedList()
list1.Mat_to_list(Mat1)
list2.Mat_to_list(Mat2)

print("===============================================")


print("VERSIÓN CON MATRICES")
print("Matriz 1")
print(Mat1)
print("Matriz 2")
print(Mat2)


print("===============================================")


print("VERSIÓN CON LISTAS")
print("Lista 1")
print(list1)
print("Lista 2")
print(list2)


print("===============================================")


print("SUMA CON MATRICES")
if(Mat1.shape == Mat2.shape):
    print(Mat1+Mat2)
else:
    print("Las matrices no tienen la misma dimensión")
print("SUMA CON LISTAS")
if(list1.head.n == list2.head.n and list1.head.m == list2.head.m):
    print(additionLinkedList(list1,list2).List_to_Mat())
else:
    print("Las listas no tienen la misma dimensión")


print("===============================================")


print("RESTA CON MATRICES")
if(Mat1.shape == Mat2.shape):
    print(Mat1-Mat2)
else:
    print("Las matrices no tienen la misma dimensión")
print("RESTA CON LISTAS")
if(list1.head.n == list2.head.n and list1.head.m == list2.head.m):
    print(subtractLinkedList(list1,list2).List_to_Mat())
else:
    print("Las listas no tienen la misma dimensión")


print("===============================================")


print("MULTIPLICACIÓN CON MATRICES")
if(Mat1.shape[1] == Mat2.shape[0]):
    print(Mat1.dot(Mat2))
else:
    print("Las matrices no se pueden multiplicar")
print("MULTIPLICACIÓN CON LISTAS")
if(list1.head.m == list2.head.n):
    print(multiply(list1,list2).List_to_Mat())
else:
    print("Las listas no se pueden multiplicar")


print("===============================================")


print("DETERMINANTE CON MATRICES")
if(Mat1.shape[1] == Mat1.shape[0]):
    print(round(np.linalg.det(Mat1)))
else:
    print("Las matriz no es cuadrada")
print("DETERMINANTE CON LISTAS")
if(list1.head.m == list1.head.n):
    print(round(Determinat(list1)))
else:
    print("Las lista no es cuadrada")