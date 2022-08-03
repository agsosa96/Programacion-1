#Desarrollar una funcion que reciba tres numeros enteros positivos y verifique
#si corresponden a una fecha valida (dia, mes, año). Devolver True o False segun
#la fecha sea correcta o no.

def validacion_de_fechas(dia,mes,anio):
    validez = False
    if(dia >= 0 and dia <= 30):
        if(mes >= 0 and mes <=12):
            
            validez = True

    return validez

d = int(input("Ingrese un dia para validar la fecha: "))
m = int(input("Ingrese un mes para validar la fecha: "))
a = int(input("Ingrese un año para validar la fecha: "))

validar = validacion_de_fechas(d,m,a)

if(validar == True):
    print("La fecha ingresada es correcta")
else:
    print("La fecha es invalida")


'''
Realizar tambien un programa para verificar el comportamiento de la funcion
'''
