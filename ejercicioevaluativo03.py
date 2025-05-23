# En un delivery de Sushi vende 4 tipos de Sushi:
# 1. Pikachu Roll $4500
# 2. Otaku Roll $5000
# 3. Pulpo Venenoso Roll $5200
# 4. Anguila Eléctrica Roll $4800
# La empresa le ha solicitado a usted, que genere una pequeña aplicación en Python para tomar el pedido de un
# cliente el cuál puede ir agregando Rolls a través de un menú uno por uno con solo seleccionar la opción (1 a 4)
# La aplicación debe mostrar en un menú los Rolls que agregará el usuario, esto se debe repetir hasta que el usuario
# decida que su pedido está completo.
# Luego de ello, debe preguntar al usuario si posee un código de descuento. En caso de que posea el código, deberá
# ingresarlo. Si el código ingresado es “soyotaku”, debe realizar un 10% de descuento al total del pedido, en caso
# contrario enviar el mensaje “código no válido” y dar al usuario la opción de reingresar el código o volver al menú
# tecleando “X”
# Una vez realizado los pasos anteriores, debe mostrar el detalle del pedido contabilizando el total de productos y la
# cantidad de cada uno de ellos y si aplica o no el descuento
total=0
articulos=0
descuento="soyotaku" 
while True:
    op=int(input("""que desea comprar?
                    1- Pikachu roll $4500
                    2- Otaku roll $5000
                    3- Pulpo venenoso roll $5200
                    4- Aguila electrica roll $4800
                    5- salir 
                    """))
  
    match op:
                case 1:
                    print("Pikachu roll ")
                    total=total+4500
                    articulos=articulos+1
                case 2:
                    print("otaku roll ")
                    total=total+5000
                    articulos=articulos+1
                case 3:
                    print("Pulpo venenoso roll ")
                    total=total+5200
                    articulos=articulos+1
                case 4: 
                    print("Aguila electrica roll ") 
                    total=total+4800
                    articulos=articulos+1 
                case 5:
                    print("saliendo....")
                    break   
                case _:
                    print("opcion invalida ")
desc=input("ingrese el codigo de descuento ")
if desc=="soyotaku":
    total=total*0.9
else:
    print("no tiene descuento")  
print("su total de articulos es ", articulos)
print("su monto total es", total)                   
