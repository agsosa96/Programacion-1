#Escribir una funcion que reciba una lista como parametro y devuelva True si la
#lista esta ordenada en forma ascendente o False en caso contrario. Por ejemplo,
#ordenada ([1, 2, 3]) retorna True y ordenada (['b', 'a']) retorna False.
#Desarrollar ademas un programa para verificar el comportamiento de la funcion.

def comprovacion(lista):
    resultado = True
    for i in range(len(lista)-1):
        if(lista[i] > lista[i+1]):
            resultado = False
            break

    return resultado

#Programa principal
prueba = [1, 2, 3]
valor = comprovacion(prueba)
if(valor != True):
    print("La lista no esta ordenada")
else:
    print("La lista esta ordenada en forma ascendente")
        

