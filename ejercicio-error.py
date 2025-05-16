name=input("ingrese su nombre ")
total=0
totaliva=0
articulos=0
while True:
    op=int(input("""que desea comprar?
                            1- arroz $1200
                            2- fideos $1000
                            3- salsa $900
                            4- azucar $1100
                            5- salir 
                            """))

    match op:
            case 1:
                print("arroz ")
                total=total+1200
                articulos=articulos+1
            case 2:
                print("fideos ")
                total=total+1000
                articulos=articulos+1
            case 3:
                print("salsa ")
                total=total+900
                articulos=articulos+1
            case 4: 
                print("azucar ") 
                total=total+1100
                articulos=articulos+1 
            case 5:
                print("saliendo....")
                break   
            case _:
                print("opcion invalida ")      
print("su total neto es ", total)  
totaliva=total*0.19
print("la cantidad de articulos que lleva es ",articulos)
print( name, "su total con iva es ",total+totaliva)  

