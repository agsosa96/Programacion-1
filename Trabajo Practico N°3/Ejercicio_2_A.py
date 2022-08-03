#Para cada un de las siguiente matrices, desarrollar una funcion que la genere y
#escribir un programa que invoque a cada una de ellas y muestre por pantalla la 
#m,atriz obtenida. El tamano de las matrices debe establecerse como N x N, y las
#funciones deben servir aunque este valor se modifique.

#a)                          1   0   0   0 
#                            0   3   0   0
#                            0   0   5   0
#                            0   0   0   7 


def crear_matriz(matrix,valor):
    filas = valor
    columnas = valor
    matrix = [[0] * columnas for i in range(filas)]

    return matrix

def diagonal_matriz(matrix):
    valor = 1
    filas = len(matrix)
    columnas = len(matrix[0])
    for f in range(filas):
        for c in range(columnas):
            if(f == c):
                matrix[f][c] = valor
                valor = valor + 2

def imprimir_matriz(matrix):
    filas = len(matrix)
    columnas = len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matrix[f][c], end="")
        print()

#Programa principal        
matriz =[]
numero = int(input("Ingrese el tamano de la matriz: "))
matriz = crear_matriz(matriz,numero)
diagonal_matriz(matriz)
imprimir_matriz(matriz)
