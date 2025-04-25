clave=1234
intentos=0
intmaximos=5

while intentos < intmaximos:
    contraseña=int(input("ingrese su contraseña"))
    if clave==contraseña:
        print("contraseña valida, bienvenido")
        break
    else: 
        print("error, contraseña invalida")
        intentos+=1
if intentos==intmaximos: 
    print("has superado el maximo de intentos")
       