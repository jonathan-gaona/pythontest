n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: "))

while n2<n1:
    print("asegurese que el numero sea mayor al anterior: ")
    n2=int(input("ingrese otro numero: ")) 



import random

n3=random.randint(n1,n2)
print("el numero random entre ambos es: ",n3)
print("    ")
print("▄"*n3)
