#Desarrollar cada una de las siguientes funciones y escribir un programa que
#permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada
#funcion:
#    a. Cargar una lista con numeros al azar de cuatro digitos. La cantidad de
#    elementos tambien sera un numero al azar de dos digitos.
#    b. Calcular y devolver la sumatoria de todos los elementos de la lista
#    anterior.
#    c. Eliminar todos las apariciones de un valor en la lista anterior. El valor
#    a eliminar se ingresa desde el teclado y la funcion lo recibe como
#    parametro.
#    d. Determinar si el contenido de una lista cualquiera es capicua, sin usar
#    listas auxiliares. Un ejemplo de lista capicua es [50, 17, 91, 17, 50].

import random

def cargar(lista,num):
    while(len(lista) < num):
        valor = random.randint(1,9)
        lista.append(valor)
        
    return lista

def sumar_lista(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
        
    return suma
    
#Programa principal
lista = []
tamanio = random.randint(1,15)
print("El tanaño de la lista es:",tamanio)
lista_cargada = cargar(lista,tamanio)
print("Los valores de la lista son:", lista_cargada)
suma = sumar_lista(lista)
print("La suma de todos los numeros de la lista es:", suma)