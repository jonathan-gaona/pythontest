
ing=int(input("ingrese sus ingresos mensuales: "))
descuento=0


if ing >=500000 and ing <=1000000:
    descuento+=300000
    print("su credito es: $300.000" )
elif ing>=1000000 and ing<=1500000:
    descuento+=650000
    print("su credito es: $650.000" )
elif ing>1500001:
    descuento+=1000000
    print("su credito es: $1.000.000" )
else:
    print("seleccion invalida")

edu=int(input("ingrese su nivel educacional: 1- basico 2-medio 3-superior: "))   

if edu==1:
    descuento=descuento*1
    print("su credito de momento es: ", descuento)
elif edu==2:
    descuento=descuento*1.3
    print("su credito de momento es: ", descuento)    
if edu==3:
    descuento=descuento*1.5
    print("su credito de momento es: ", descuento)
else: 
    print("seleccion invalida: ")  

naci=int(input("ingrese su nacionalidad: 1-chilena 2-extrangera: " ))

if naci==1:
    descuento+=300000
    print("su credito total es: ", descuento)
elif naci==2:
    descuento+=0
    print("su credito total es: ", descuento)

