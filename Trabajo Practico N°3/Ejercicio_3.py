#Desarrollar un programa para rellenar una matriz de N x N con numeros enteros 
#al azar comprendidos en el intervalo [0,N^2], de tal forma que ningun numero se
#repita. Imprimir la matriz por pantalla.

import random

def crear_matriz(matrix,valor):
    fila = valor
    columna = valor
    matrix = [[0] * columna for i in range(fila)]

    return matrix

def rellenar_matriz(matrix,valor):
    filas = len(matrix)
    columnas = len(matrix[0])
    for f in range(filas):
        for c in range(columnas):
            matrix[f][c] = random.randint(0,valor ** 2)

def escribir_matriz(matrix):
    fila = len(matrix)
    columna = len(matrix[0])
    for f in range(fila):
        for c in range(columna):
            print("%3d" %matrix[f][c], end="")
        print()

#Programa Pricipal
matriz = []
numero = int(input("Ingrese el tamaño de la matriz: "))
matriz = crear_matriz(matriz,numero)
rellenar_matriz(matriz,numero)
escribir_matriz(matriz)
