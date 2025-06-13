
# diccionarios son conjunto de pares de datos

# dic={
#     "nombre": "david",
#     "numero": 32132132,
#     "casado" : True 
# } 
# print(dic()) 
# print(dic["nombre"]) 

# for key, value in dic.items():
#     print(key,value)

# --------------------------------------


# frutas={
#     "manzana": 1500,
#     "frutilla": 1600,
#     "durazno": 3800
# }

# print(frutas)
# frutas["pera"]= 1200

# print(frutas)

# fru=input("ingrese la fruta ")
# val=input("ingrese el precio ")
# frutas[fru]=val
# print(frutas)

# -------------------------------

frutas={}
op=int(input(print("""que desea hacer?
1- Ingresar fruta y precio
2- Actualizar precio
3- borrar fruta y precio
4- mostrar todas las frutas y precios 
5- salir 
""")))
match op:
    case 1:
        fru=input("ingrese la fruta ")
        val=input("ingrese el precio ")
    case 2:
        print(frutas)
        frutas[fru]=val
        print(frutas)
    case 3:
        print(frutas)
        fru=input("ingrese la fruta a eliminar ")
        frutas.pop[fru]
    case 4:
        print(frutas)
    case 5:
        print("saliendo..")
    case _:
        print("opcion invalida")

