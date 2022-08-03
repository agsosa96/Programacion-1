#Para cada un de las siguiente matrices, desarrollar una funcion que la genere y
#escribir un programa que invoque a cada una de ellas y muestre por pantalla la 
#m,atriz obtenida. El tamano de las matrices debe establecerse como N x N, y las
#funciones deben servir aunque este valor se modifique.

#d)                          8   8   8   8 
#                            4   4   4   4
#                            2   2   2   2
#                            1   1   1   1 

def crear_matriz(matrix,valor):
    filas = valor
    columnas = valor
    matrix = [[0] * columnas for i in range(filas)]

    return matrix

def escribir_matriz(matrix):
    filas = 0
    columnas = len(matrix[0])
    valor = len(matrix) - 1
    for f in range(len(matrix)):
        for c in range(columnas): 
            matrix[f][c] = 2 ** valor
        valor = valor - 1
        filas = filas + 1

def imprimir_matriz(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matrix[f][c], end="")
        print()

#Programa Principal
matriz = []
numero = int(input("Ingrese el tamaño de la matriz: "))
matriz = crear_matriz(matriz,numero)
escribir_matriz(matriz)
imprimir_matriz(matriz)
    
