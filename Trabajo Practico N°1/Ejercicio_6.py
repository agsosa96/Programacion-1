#Desarrollar una funcion que reciba como parametros dos numeros enteros positivos
#y devuelva el numero que resulte de concatenar ambos valores. Por ejemplo, si
#recibe 1234 y 567 devolver 1234567. No se permite utilizar facilidades de Python
#no vistas en clase.


def concatenador(num_1,num_2):
    cont = 0
    aux = num_2
    while(aux > 0):
        aux = aux // 10
        cont = cont + 1
    num_1 = num_1 * (10 ** cont)
    concatenacion = num_1 + num_2
    
    return concatenacion 

pimer_numero = int(input("Ingrese el primero numero: "))
segundo_numero = int(input("Ingrese el primero numero: "))

valor = concatenador(pimer_numero,segundo_numero)

print("La contacion seria:",valor)

input()
