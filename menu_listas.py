
nombres=["joni",]
apellidos=["campeón"]
while True:
    print("""
        1- Ingresar nombre
        2- Buscar nombre
        3- Mostrar lista
        4- Salir
        """)
    op=int(input("seleccione una opcion "))
    match op:
        case 1:
            nom=input("ingrese su nombre")
            nombres.append(nom)
            ap=input("ingrese su apellido")
            apellidos.append(ap)
            # print(nombres)
        case 2:
            nombus=input("ingrese un nombre a buscar")
            if nombus in nombres:
                print("el nombre",nombus, "exixte en la lista")
            else:
                print("el nombre",nombus, "no exixte en la lista ")
        case 3:
            cont=0
            for n in nombres:
                print(cont+1,"-.",nombres[cont],apellidos[cont] )
            # otra forma es:
            # for i in range(len(nombres)):
            #     print(i+1, ".-",nombres[i], apellidos[i])
        case 4:
            print("saliendo..")
            break
        case _:
            print("opcion invalida")