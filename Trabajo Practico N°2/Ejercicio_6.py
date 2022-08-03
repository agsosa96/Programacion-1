#Escribir una funcion que reciba una lista de numeros enteros como parametros y
#la normalice, es decir que todos sus elementos debe sumar 1.0, respetando las
#proprociones relativas que cada elemento tiene en la lista original.
#Desarollar tambien un programa que permita el comportamiento de la funcion. Por
#ejemplo, normalizar ([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].

def normalizar_lista(num,lista):
    for i in range(len(lista)):
        lista[i] = lista [i] / num
    
    return lista

#Programa principal
numeros = [1, 1, 2]
suma = sum(numeros)
normalizada = normalizar_lista(suma,numeros)
print("La lista normaliza es: ", normalizada)


