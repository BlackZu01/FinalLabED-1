import tkinter as tk
from tkinter import ttk
import numpy as np
from classes import *

class App(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        
        self.dato = tk.StringVar()
        self.nombre_archivo = ttk.Label(ventana, text='Nombre del archivo: ')
        self.nombre_archivo.place(x=20, y=23)

        self.dato2 = tk.StringVar()
        self.nombre_archivo2 = ttk.Label(ventana, text='Nombre del archivo 2: ')
        self.nombre_archivo2.place(x=20, y=64)

        self.nota = ttk.Label(ventana, 
                              text='Nota: Sólo ingrese el nombre de archivo 2 si va a \nrealizar operaciones como (suma, resta, multiplicación)')
        self.nota.place(x=20 , y=130)

        self.escalar = tk.StringVar()
        self.escalar_texto = ttk.Label(ventana, text='Escalar: ')
        self.escalar_texto.place(x=20, y=105)

        self.escalar_caja = ttk.Entry(ventana, textvariable=self.escalar)
        self.escalar_caja.place(x=170, y=100, width=150, height=27)
        self.boton_nombre3 = ttk.Button(ventana, text= 'Enviar')
        self.boton_nombre3.place(x= 330, y=100)


        self.caja_nombre = ttk.Entry(ventana, textvariable=self.dato)
        self.caja_nombre.place(x=170, y=20, width=150, height=27)

        self.caja_nombre2 = ttk.Entry(ventana, textvariable=self.dato2)
        self.caja_nombre2.place(x=170, y=60, width=150, height=27)

        self.boton_nombre = ttk.Button(ventana, text='Enviar')
        self.boton_nombre.place(x= 330, y=20)

        self.boton_nombre2 = ttk.Button(ventana, text='Enviar')
        self.boton_nombre2.place(x= 330, y=60)

        self.opciones = ttk.Label(ventana, text=' OPCIONES')
        self.opciones.place(x = 300, y=200)

        self.suma = ttk.Button(ventana, text='Suma', command=self.suma)
        self.suma.place(x=130, y=230)

        self.resta = ttk.Button(ventana, text='Resta', command=self.resta)
        self.resta.place(x=230, y=230)

        self.mult = ttk.Button(ventana, text='Multiplicación', command=self.mult)
        self.mult.place(x=330, y=230)

        self.det = ttk.Button(ventana, text='Determinante', command=self.determinante)
        self.det.place(x=450, y=230)

        self.det = ttk.Button(ventana, text='Escalar', command=self.escalarProd)
        self.det.place(x=280, y=270)

        self.det_text = ttk.Label(ventana, 
                                  text='Determinante: ')
        self.det_text.place(x=20, y=300)
    
    def suma(self):
        try:
            self.matrix_uno = np.loadtxt(self.dato.get())
            self.matrix_dos = np.loadtxt(self.dato2.get())
            self.lista1 = LinkedList()
            self.lista2 = LinkedList()
            self.lista1.Mat_to_list(self.matrix_uno)
            self.lista2.Mat_to_list(self.matrix_dos)
            self.matrix_suma = additionLinkedList(self.lista1, self.lista2)

            np.savetxt('Suma.txt', self.matrix_suma.List_to_Mat(), fmt='% 4d')
        except AttributeError:
            print('Las dimensiones no coinciden')
    def resta(self):
        try:
            self.matrix_uno = np.loadtxt(self.dato.get())
            self.matrix_dos = np.loadtxt(self.dato2.get())
            self.lista1 = LinkedList()
            self.lista2 = LinkedList()
            self.lista1.Mat_to_list(self.matrix_uno)
            self.lista2.Mat_to_list(self.matrix_dos)
            self.matrix_resta = subtractLinkedList(self.lista1, self.lista2)
            np.savetxt('Resta.txt', self.matrix_resta.List_to_Mat(), fmt='% 4d')
        except AttributeError:
            print('Las dimensiones no coinciden')
    
    def mult(self):
        try:
            self.matrix_uno = np.loadtxt(self.dato.get())
            self.matrix_dos = np.loadtxt(self.dato2.get())
            self.lista1 = LinkedList()
            self.lista2 = LinkedList()
            self.lista1.Mat_to_list(self.matrix_uno)
            self.lista2.Mat_to_list(self.matrix_dos)
            self.matrix_mult = multiply(self.lista1, self.lista2)
            np.savetxt('Multiplicacion.txt', self.matrix_mult.List_to_Mat(), fmt='% 4d')
        except AttributeError:
            print('Las dimensiones no coinciden')

    def determinante(self):
        self.matrix_uno = np.loadtxt(self.dato.get())
        self.lista = LinkedList()
        self.lista.Mat_to_list(self.matrix_uno)
        self.deter = Determinat(self.lista)
        self.det_text.config(text=f'Determinante: {self.deter}')

    def escalarProd(self):
        self.matrix_uno = np.loadtxt(self.dato.get())
        self.lista = LinkedList()
        self.lista.Mat_to_list(self.matrix_uno)
        self.escalarprod = multiplywithn(self.lista, int(self.escalar.get()))
        np.savetxt('MultiplicacionEscalar.txt', self.lista.List_to_Mat(), fmt='% 4d')
        

ventana = tk.Tk()
ventana.title('Operaciones con matrices')
ventana.config(width=700, height=600)
app = App(ventana)

ventana.mainloop()