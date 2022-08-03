#Un comercio de electrodomesticos necesita para su linea de cajas un programa que
#la indique al cajero el cambio de que debe entregarle al cliente. Para eso se
#ingresan dos numeros enteros, correspondientes al total de la compra y el dinero
#recibio. Informar cuantos billetes de cadad denominacion deben ser entregados al
#cliente como vuelto, de tal forma que se minimice la cantidad de billetes.
#Considerar que exiten billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un
#mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: Si la compra
#es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1
#billete de $50, 1 billte de $20, 1 billete de $10 y 3 billetes de $1.


def cambio (compra,dinero):
    vuelto = dinero - compra
    
    quinientos = vuelto // 500
    print("La cantidad de $500 son:",quinientos)
    
    cien = (vuelto - quinientos * 500)// 100
    print("La cantidad de $100 son:",cien)
    
    cincuenta = (vuelto - quinientos * 500 - cien * 100)// 50
    print("La cantidad de $50 son:",cincuenta)

    veinte = (vuelto - quinientos * 500 - cien * 100 - cincuenta * 50)// 20
    print("La cantidad de $20 son:",veinte)
    
    diez = (vuelto - quinientos * 500 - cien * 100 - cincuenta * 50 - veinte * 20)// 10
    print("La cantidad de $10 son:",diez)
    
    cinco = (vuelto - quinientos * 500 - cien * 100 - cincuenta * 50 - veinte * 20 - diez * 10)// 5
    print("La cantidad de $5 son:",cinco)
    
    uno = (vuelto - quinientos * 500 - cien * 100 - cincuenta * 50 - veinte * 20 - diez * 10 - cinco * 5 )// 1
    print("La cantidad de $1 son:",uno)
    

valor_compra = int(input("Ingrese el monto de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

if(valor_compra > dinero_recibido):
    print("El dinero recibido es insuficiente")
else:
    cambio(valor_compra,dinero_recibido)
