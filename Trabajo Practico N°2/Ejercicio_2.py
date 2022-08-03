#Escribir funciones para:
#    a. Generar una lista de 50 numeros aleatorios del 1 al 100.
#    b. Recibir una lista como parametro y devolver True si la misma contiene
#    algun elemento repedido. La funcion no debe modificar la lista.
#    c. Recibir una lista como parametro y devolver una nueva lista con los
#    elementos unicos de la lista original, sin importar el orden.

#Conmibar estas tres funciones en un mismo programa.

import random

def cargar_lista(valor):
    for i in range(50):
        numero = random.randint(1,100)
        lista.append(numero)

def repetido(valor):
    resultado = True
    for i in range(len(lista)):
        if(valor.count(i)>1):
            resultado = False
            
    return resultado

def lista_nueva(valor):
    lista2 = []
    for i in range(len(lista)):
        numero = valor.count(i)
        if(numero == 0):
            lista2.append(valor[i])

    return lista2

#Programa principal
lista = []
cargar_lista(lista)
print(lista)

print()

comprobar = repetido(lista)
if(comprobar == True):
    print("No hay numero repetidos en la lista")
else:
    print("Hay numero repetidos en la lista")

print()
nueva_lista = lista_nueva(lista)
print(nueva_lista)
