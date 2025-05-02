# total=0
# cant=int(input("cuantos productos llevara?"))

# for i in range (cant):
#     print('''
#     que productos llevara?
#     1- diazepam $9000
#     2- metametazona $18500
#     3- oblea china $1000 ''')
#     op=int(input())
#     if op==1: 
#         print("usted llevara diazepam")
#         total=total+9000
#     elif op==2:
#         print("usted lleva metametazona")
#         total=total+18500
#     elif op==3:
#         print("usted lleva oblea china")
#         total=total+1000
# print("el total neto es ", total)
# print("total mas iva es ", total*1.19) 

import time
palabra="catolica"
cont=0
vocales=0
for i in palabra.lower:
    print(i)
    cont=cont+1
    time.sleep(1)
    if i in "aeiou":
        vocales=vocales+1
        # vocales+=1
print("la cantidad de caracteres son", cont)
print("la cantidad de vocales son", vocales)