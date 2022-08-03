#Desarrollar una funcion que reciba tres numeros positivos y devuelva el mayor 
#de los tres, solo si este es unico (estricto). En caso de no existir el mayor 
#es estricto devolver -1. No utilizar operadores logicos (and, or , not)

def seleccionador_mayor (num_1,num_2,num_3):
    valor = -1
    if(num_1 > num_2):
        if(num_1 > num_3):
            valor = num_1      
    if(valor == -1):
        if(num_2 > num_3):
            valor = num_2
        if(num_3 > num_2):
            valor = num_3

    return valor

num_1 = int(input("Ingrese el primer positivo valor a comparar: "))
num_2 = int(input("Ingrese el segundo positivo valor a comparar: "))
num_3 = int(input("Ingrese el tercer positivo valor a comparar: "))

mayor = seleccionador_mayor (num_1,num_2,num_3)
print("El mayor es (En caso de no haber mayor devuelve -1): ", mayor)


#Desarrollar tambien un programa para ingresar los tres valores, invocar a la
#funcion y mostrar el maximo hallado, o un mensaje informativo si este no
#existe.

def seleccionador_mayor (num_1,num_2,num_3):
    valor = -1
    if(num_1 > num_2):
        if(num_1 > num_3):
            valor = num_1      
    if(valor == -1):
        if(num_2 > num_3):
            valor = num_2
        if(num_3 > num_2):
            valor = num_3

    return valor

num_1 = int(input("Ingrese el primer positivo valor a comparar: "))
num_2 = int(input("Ingrese el segundo positivo valor a comparar: "))
num_3 = int(input("Ingrese el tercer positivo valor a comparar: "))

mayor = seleccionador_mayor (num_1,num_2,num_3)

if(mayor == -1):
    print("El maximo absoluto no existe")
else:
    print("El mayor es (En caso de no haber mayor devuelve -1): ", mayor)

input()
