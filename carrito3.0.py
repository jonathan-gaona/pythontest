# crear carrito 3.0 
# tomar el carrito de compras anterior y hacerlo con listas
# 1 ingresar el producto 
# 2 comprar
# 3 crear boleta
# 4 salir
# que el carrito comienze con 3 productos
# hay que hacer 3 listas, produtos, precios y carrito


# productos=["Disco SSD 1TB", "Memoria Ram 8GB", "Mouse"]
# precios=[70000, 30000, 15000]
# carrito=[]

# while True:
#     while True:
#         try:
#             print('''
#                 1.- Ingresar productos a la tienda
#                 2.- Comprar
#                 3.- Crear Boleta
#                 4.- Salir
#                 ''')
#             op=int(input("Ingese una opcion: "))
#             break
#         except Exception:
#              print("Ingrese un numero entero válido")
#     match op:
#         case 1:
#             pro=input("Ingrese el nombre del Producto: ")
#             productos.append(pro)
#             pre=int(input("Ingrese el Precio: "))
#             precios.append(pre)
#         case 2:
#                 for i in range(len(productos)):
#                     print(i+1, ".-", productos[i], "$", precios[i] )
#                 pro=int(input("Selecione que quiere comprar: "))
#                 carrito.append(pro-1)
#                 print(carrito)
#         case 3:
#             total=0
#             print("---------------0----------------")
#             print("Bienvenido a PC House ")
#             for i in carrito:
#                   print( productos[i], "----- $", precios[i] )
#                   total=total+precios[i]
#             print("Es total de articulos es", len(carrito))
#             print("Su total neto es ", total)
#             print("Su total mas iva es ", total*1.19)
#             print("---------------0----------------")

#         case 4:
#             print("Saliendo")
#             break
#         case _:
#             print("opcion invalida")


# ---------------------------------------------


# crear programa de manejo de notas 
# 1 ingresar nota 
# 2 borrar notas
# 3 mostrar notas
# 4 sacar promedio, nota mayor y menor 
# 5 limpiar todas las notas
# 6 salir 

# -----------------------------------------

notas=[]
promedio=0
while True:
    while True:
        try:
            print('''
                1.- Ingresar nota
                2.- Borrar nota
                3.- Mostrar notas 
                4.- Sacar promedio 
                5.- Limpiar todas las notas
                6.- Salir
                ''')
            op=int(input("Ingese una opcion: "))
            break
        except Exception:
             print("Ingrese un numero entero válido")
    match op:
         case 1:
              nota=float(input("ingrese su nota "))
              notas.append(nota)
         case 2:
            for num, n in enumerate(notas):
                print(num+1,".- ",n)
            elim=int(input("ingrese cual quiere eliminar: "))
            notas.pop(elim-1)
         case 3:
              for i in notas:
                   print(i)
              print("su nota maxima fue: ",max(notas))
              print("su nota minima fue: ",min(notas))
         case 4:
              if len(notas)==0:
                   print("no hay notas para sacar promedio")
              else:
                promedio=sum(notas) / len(notas)
                print("su promedio es: ",round(promedio,1))
         case 5:
              notas.clear
              print("se eliminaron todas las notas")
         case 6:
              print("saliendo...")
              break
         case _:
              print("opcion invalida")