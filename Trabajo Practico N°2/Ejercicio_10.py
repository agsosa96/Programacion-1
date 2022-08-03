#Generar un lista con numeros al azar entre 1 y 100 y crear una nueva lista con
#los elementos de la primera que sean impares. El proceso debera realizarse
#utilizando listas por compresion. Imprimir las dos listas por pantalla.

import random

def numeros_azar(lista):
    while(len(lista)<10):
        num = random.randint(1,100)
        lista.append(num)
    
    return lista 

def numeros_impares(lista):
    lista = [i for i in lista if i%2 != 0]

    return lista

#Programa principal
num = []
numeros_cargados = numeros_azar(num)
print(numeros_cargados)
print(numeros_impares(numeros_cargados))
