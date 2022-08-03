#Una persona desea llevar el control de los gastos realizafos al viajar en el
#subterraneo dentro de un mes. Sabiendo que dicho medio transporte utiliza un
#esquema de tarifa decrecientes (detalladas en la tabla de abajo) se solicita
#desarrollar una funcion que reciba como parametro la cantidad de viajes
#realizados en un determinado mes y devuelva el total gastado en viajes.
#Realizar tambien un programa para verificar el comportamiento de la funcion


def gastos_tarifa (viajes,valor):
    if(viajes < 20):
        gastos = viajes * valor
    elif(viajes > 20 and viajes < 30):
        gastos = (viajes - 20) * (0.8 * valor) + 20 * valor
    elif(viajes > 30 and viajes < 40):
        gastos = (viajes - 30) * (0.7 * valor) + 10 * (0.8 * valor) + 20 * valor
    elif(viajes > 40):
        gastos = (viajes - 40) * (0.6 * valor) + 10 * (0.7 * valor) + 10 * (0.8 * valor) + 20 * valor

    return gastos


cantidad_viajes = int(input("Ingrese la cantidad de viajes realizados: "))
valor_tarifa = int(input("Ingrese el valor de la tarifa: "))

print("Los gastos realizados son: ",gastos_tarifa (cantidad_viajes,valor_tarifa))

input
