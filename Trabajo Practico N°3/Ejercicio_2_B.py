#Para cada un de las siguiente matrices, desarrollar una funcion que la genere y
#escribir un programa que invoque a cada una de ellas y muestre por pantalla la 
#m,atriz obtenida. El tamano de las matrices debe establecerse como N x N, y las
#funciones deben servir aunque este valor se modifique.

#b)                          0   0   0   27 
#                            0   0   5   0
#                            0   3   0   0
#                            1   0   0   0 

def crear_matriz(matrix,valor):
    filas = valor
    columnas = valor
    matrix = [[0] * columnas for i in range (filas)]

    return matrix

def diagonal_inversa(matrix):
    fila = len(matrix) - 1 
    columna = 0
    potencia = 0
    for c in range(len(matrix[0])):
        if(c == columna):
            for f in range(len(matrix)):
                if(f == fila):
                    matrix[f][c] = 3 ** potencia
                    fila = fila - 1    
                    columna = columna + 1
                    potencia = potencia + 1
    
def imprimir_matriz(matrix):
    filas = len(matrix)
    columna = len(matrix[0])
    for f in range(filas):
        for c in range(columna):
            print("%3d" %matrix[f][c], end="")
        print()


#Programa principal
matriz =[]
numero = int(input("Ingrese el tamaño de la matriz: "))
matriz = crear_matriz(matriz,numero)
diagonal_inversa(matriz)
imprimir_matriz(matriz)
