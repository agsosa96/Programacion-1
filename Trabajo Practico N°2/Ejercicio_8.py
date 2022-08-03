#Utilizar la tecnica de listas por compresion para construir una lista con todos
#los numeros impares comprendidos entre 100 y 200.

def numeros_impares(lista):
    lista=[i for i in range(100,201) if i%2!=0]

    return lista

#programa principal
impares= []
numeros = numeros_impares(impares)
print(numeros)
