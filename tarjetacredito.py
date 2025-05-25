deuda=100000
saldo=0
def menu():
    print("""---Menu principal---
        1- Pago de tarjeta de credito
        2- Simulacion de compra
        3- Salir
        """)
menu()
op=int(input("selecione la opcion requerida (1-3) "))

while True:
    if op==1:
        print("su deuda actual es: $",deuda)
        pago=int(input("digite el monto a pagar: $ "))
        if pago<0:
            print("digite un monto valido")
        elif pago>100000:
            print("error, el monto ingresado exede el monto maximo de deuda")
        else:
            deuda=deuda-pago
            saldo=saldo+pago
            print("pago realizado su nueva deuda es: $",deuda)
            print("Su nuevo saldo es: $",saldo)
    elif op==2:
        while True:
            print("su saldo actual es: $",saldo)
            monto_compra=input("digite el monto de su compra o precione x para volver al menu ")
            if monto_compra =="x":
                break
            if monto_compra<"0":
                print("el monto debe ser mayor a 0")
            elif monto_compra>saldo:
                print("error, saldo insuficiente")
            else:
                saldo=saldo-monto_compra
                deuda=deuda-monto_compra
                print("compra realizada nuevo saldo de tarjeta",saldo)
    elif op==3:
        print("saliendo del programa...")
        break
    else:
        print("opcion invalida, seleccione una opcion del 1-3")       




