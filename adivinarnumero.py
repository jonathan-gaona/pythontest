import random

numero1 = random.randint(1,50)

num=int (input("ingrese un numero a adivinar: "))
while num!=numero1:
    if num>numero1:
        num=int (input("su numero es menor, ingrese otro numero a adivinar: "))
    else:
        num=int (input("su numero es mayor, ingrese otro numero a adivinar: "))
print("adivino el numero")
    