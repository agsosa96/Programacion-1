#Escribir dos funciones separadas para imprimir por pantalla los siguientes
#patrones de asterisocos, donde la cnatidad de filas se recibe como parametro:
#
#                **********                     **
#                **********                     ****
#                **********                     ******
#                **********                     ********
#                **********                     **********

def asteriscos(num_filas):
    for i in range(num_filas):
        print("**********")

def asteriscos_escaleras(num_filas):
    contador = 1
    for i in range(num_filas):
        for j in range(contador):
            print("**",end="")
        contador = contador + 1
        print()

filas = int(input("Ingrese el numero de filas: "))
print()

asteriscos(filas)
print()
asteriscos_escaleras(filas)
