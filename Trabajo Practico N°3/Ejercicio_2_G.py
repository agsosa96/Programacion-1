#Para cada un de las siguiente matrices, desarrollar una funcion que la genere y
#escribir un programa que invoque a cada una de ellas y muestre por pantalla la 
#m,atriz obtenida. El tamano de las matrices debe establecerse como N x N, y las
#funciones deben servir aunque este valor se modifique.

#g)                          1   2   3   4 
#                           12  13  14   5
#                           11  16  15   6
#                           10   9   8   7 

def crear_matriz(matrix,valor):
    filas = valor
    columnas = valor
    matrix = [[0] * columnas for i in range(filas)]

    return matrix

def espiral(matrix):
    fila = 0
    columna = 0
    direccion = 0
    movimiento = 0
    contador = 1
    limite = len(matrix) - 1
    for i in range(len(matrix)**2):
        
        matrix[fila][columna] = contador
        contador = contador + 1
        movimiento = movimiento + 1

        if(movimiento > limite):
            movimiento = 0
            direccion = direccion + 1
            if(direccion == 3 or direccion == 1):
                limite = limite - 1

        if(direccion > 3):
            direccion = 0

        if(direccion == 0):
            columna = columna + 1
        elif(direccion == 1):
            fila = fila + 1
        elif(direccion == 2):
            columna = columna - 1
        elif(direccion == 3):
            fila = fila - 1
        
def imprimir_matriz(matrix):
    filas = len(matrix)
    columnas = len(matrix[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matrix[f][c], end="")
        print()

#Programa Principal
matriz = []
numero = int(input("Ingrese un el tamaño de la matriz: "))
matriz = crear_matriz(matriz,numero)
espiral(matriz)
imprimir_matriz(matriz)
