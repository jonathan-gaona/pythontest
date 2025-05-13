# uso de match 

import random
import time


def suma():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es: ", n1+n2)

def resta():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la resta es: ", n1-n2)

def divi():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la division es: ", n1/n2)

def multi():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la multiplicacion es: ", n1*n2)

def calculadora():
    while True:
        op=int(input("""ingrese una opcion
                    1- suma
                    2- resta
                    3- multiplicacion
                    4- division 
                    5- salir 
                    """))
        match op:
            case 1:
                print("suma ")
                suma()
            case 2:
                print("resta ")
                resta()
            case 3:
                print("multiplicacion ")
                multi()
            case 4: 
                print("division ") 
                divi()   
            case 5:
                print("saliendo....")
                break    
            case _:
                print("opcion invalida ")
                           
def adivine():
    n1=int(input("ingrese el limite inferior a adivinar "))
    n2=int(input("ingrese el limite superior a adivinar "))
    numero1 = random.randint(n1,n2)

    num=int (input("ingrese un numero a adivinar: "))
    while num!=numero1:
        if num>numero1:
            num=int (input("su numero es menor, ingrese otro numero a adivinar: "))
        else:
            num=int (input("su numero es mayor, ingrese otro numero a adivinar: "))
    print("adivino el numero")

def ludo():
    meta=30
    turno=1
    j1=0
    j2=0
    while j1<=30 and j2<=30:
        if turno %2==0:
            print("turno de J1")
            time.sleep(1)
            dado=random.randint(1,6)
            j1=j1+dado
            turno=turno+1
            print("J1 sacó: ",dado)
            print("avanza hasta la casilla ",j1)
        else:
            print("turno de J2")
            time.sleep(1)
            dado=random.randint(1,6)
            j2= j2+dado
            turno=turno+1
            print("J2 sacó: ",dado)
            print("avanza hasta la casilla ",j2)

