# uso del while

# num=0

# while num<=5:
#     print(num)
#     num+=1

# num=10

# while num>=0:
#     print(num)
#     num-=1

# resp="no"
# while resp!= "si":
#     resp=input("desea salir del sistema?")

clave=123

contraseña=int(input( "ingrese su contraseña"))

while clave!=contraseña:
    print("error, clave invalida")
    contraseña=int(input( "ingrese su contraseña"))
print("clave correcta, bienvenido")    
