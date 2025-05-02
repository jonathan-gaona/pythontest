comuna= int (input("1-la florida(20%), 2-la pintana(30%), 3-puente alto(25%), 4-san joaquin(15%) "))

arancel=200000
descuento=0

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=30
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15 
else: 
    print("seleccion incorrecta")

grupo=int (input("ingrese su grupo familiar incluido usted: "))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif grupo>=5:
    descuento+=4
else: 
    print("seleccion incorrecta")

print("el descuento total  es ", descuento)  
desc=arancel*descuento/100
total=arancel-desc
print("total a pagar es: ",total)  