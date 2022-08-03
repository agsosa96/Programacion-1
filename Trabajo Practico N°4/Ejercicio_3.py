#Los numeros de claves de dos cajas fuertes estan intercalados dentro de un
#numero entero llamado "clavo maestra", cuya longitud no se conoce. Realizar un
#programa para obtener ambas claves, donde la primera se construye con los
#digitos ubicados en posiciones impares de la clave maestra y la segunda con los
#digitos ubicados en posiciones pares. Los digitos se numeran desde la izquierda
#.Ejemplo: Si clave maestra fuera 18293, la clave 1 seria 123 y la clave 2 seria
#89.

def separacion_clave(listaM):
    strListaM = str(listaM)
    strLista1= strListaM[::2]
    strLista2= strListaM[1::2]
    
    return int(strLista1),int(strLista2)

#Programa Principal
clave_maestra = int(input("Ingrese la clave maestra: "))
clave1 , clave2 = separacion_clave(clave_maestra)
print("La primera clave impar seria" ,clave1, "La segunda clave par seria" ,clave2)
