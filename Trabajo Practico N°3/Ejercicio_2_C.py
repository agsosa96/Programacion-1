#Para cada un de las siguiente matrices, desarrollar una funcion que la genere y
#escribir un programa que invoque a cada una de ellas y muestre por pantalla la 
#m,atriz obtenida. El tamano de las matrices debe establecerse como N x N, y las
#funciones deben servir aunque este valor se modifique.

#c)                          4   0   0   0 
#                            3   3   0   0
#                            2   2   2   0
#                            1   1   1   1 


def crear_matriz(matrix,valor):
    filas = valor
    columnas = valor
    matrix = [[0] * columnas for i in range(filas)]

    return matrix

def matriz_gradiente(matrix):
    filas = 0
    columnas = len(matrix[0])
    valor = len(matrix) + 1
    for f in range(filas):
        if(f == filas):
            for c in range(len(matrix[0])):
                if(c == columnas):
                    matrix[f][c] = valor
                columnas = columnas + 1
        filas = filas + 1

def imprimir_matriz(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matrix[f][c], end="")
        print()

#Programa principal
matriz = []
numero = int(input("Ingrese el tamaño de la matriz: "))
matriz = crear_matriz(matriz,numero)
matriz_gradiente(matriz)
imprimir_matriz(matriz)
