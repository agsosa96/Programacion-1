#Eliminar de una lista de palabra las palabras que se encuentren en una segunda
#lista. Imprimir la lista original, la lista de palabras a eliminiar y la lista
#resultante.

def eliminar_palabras(lista,eliminada):
    nueva_lista = []
    for i in range(len(eliminada)):
        for j in range(lista.count(i))
            if(eliminada[i] in lista):
                nueva_lista = lista.remove(elimada[i])

    return nueva_lista

#Programa Principal
lista = []
lista = str(input("Ingrese la lista de palabras: "))
            
