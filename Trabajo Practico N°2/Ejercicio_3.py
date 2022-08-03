#Crear una lista con los cuadrados de los numeros entre 1 y N (ambos incluidos),
#donde N se ingresa desde el teclado. Luego se solicita imprimir los ultimos 10
#valores de la lista.

def numero_cuadrado(lista,num):
    for i in range(1,num+1):
        num_cuadrado = i ** 2
        lista.append(num_cuadrado)

    return lista

def imprimir_ultimo(cuadrado):
    lista_impresion = []
    if(len(cuadrado) < 10):
        print("La lista contiene menos de 10 elementos")
    else:
        for i in range(len(cuadrado)-10,len(cuadrado)):
            valor = cuadrado[i]
            lista_impresion.append(valor)
        print(lista_impresion)

#Programa principal
lista = []
valor = int(input("Ingrese hasta que numero se va a generar el cuadrado: "))
lista_cuadrado = numero_cuadrado(lista,valor)
print(lista_cuadrado)
imprimir_ultimo(lista_cuadrado)


