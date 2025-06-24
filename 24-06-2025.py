# nuevos diccionarios y manipulacion de datos

juegos={
    1:{"nombre": "metroid dread",
       "precio": 50000,
       "code": "MMdd23"},
    2:{ "nombre": "mario bros",
       "precio": 55000,
       "code": "RRee24"},
       }

# nombre=input("ingrese el nombre del juego: ")
# precio=int(input("ingrese el precio: "))
# code=input("inrese el codigo: ")

# juegos[3]={ "nombre": nombre,
#        "precio": precio,
#        "code": code}

# for juegos , datos in juegos.items():
#     print(juegos,datos)

def mostrar_juegos(dic):
        for juegos , datos in juegos.items():
            print(juegos,datos)



while True:
    try:
        op=int(input("""que desea hacer?
        1- Ingresar juego
        2- mostrar juegos
        3- actualizar precio
        4- borrar juego
        5- salir 
        """))
        match op:
            case 1:
                nombre=input("ingrese el nombre del juego: ")
                precio=int(input("ingrese el precio: "))
                code=input("inrese el codigo: ")
                
                largo=len(juegos)
                juegos[largo+1]={ "nombre": nombre,
                            "precio": precio,
                            "code": code}
            case 2:
                for juegos , datos in juegos.items():
                    print(juegos,datos)
            case 3:
                print("")
            case 4:
                mostrar_juegos(juegos)
                eliminar=int(input("ingrese el numero del juego a borrar: "))
                del juegos[eliminar]
            case 5:
                print("saliendo..")
                break
            case _:
                print("opcion invalida")
    except Exception as e:
        print("error",e)


"""
el codigo debe tener 2 mayusculas 2 minusculas y 4 numeros
largo de 8 
"""
