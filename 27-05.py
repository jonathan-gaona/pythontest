deuda=100000
saldo=0
monto=0
while True:
    while True:
        try:
            op=int(input(""""
                        seleccione una opcion
                        1- Pagar tarjeta
                        2- Simular compra
                        3- Salir
                        """))
            break
        except Exception:
            print("solo numeros enteros entre (1-3)")    
    match op:
        case 1:
                print("su deuda actual es de: $",deuda)
                pago=int(input("Ingrese el monto a pagar: "))
                deuda=deuda-pago
                saldo=saldo+pago
                while True:
                    if pago<=0:
                        print("el monto debe ser mayor a 0")
                        break
                    elif pago>100000:
                        print("el monto no puede ser mayor a la deuda")
                        break
                    else:
                        print("el pago se realizo")
                        print("su nuevo saldo es: $",saldo) 
                        print("su deuda quedo en: $",deuda)
                        break
                                      
                        
        case 2:
            while True:
                monto_compra=int(input("ingrese el monto de su compra: "))
                monto=monto+monto_compra
                print("su monto hasta el momento es: ",monto)
                print("si desea salir escriba 00 ")
                if monto_compra == 00:
                    break
        case 3:
            print("saliendo...")
            break
        case _:
            print("opcion invalida")