# perro de caza
# pida al usuario la cantidad de perros 
# muestre cual es la cuota minima de conejos
# luego consulte cuantos conejos trajo
# si el perro trajo la cantidad minima
# cumplio la cuota, sino se queda sin Filete 
# mostrar resumen de perro que cumplieron y los que no 

import random
# while True:
#     try:
#         cuotaminima=3
#         cumplen=0
#         perros=int(input("cuantos perros trae?"))
#         print("la cuota minima de conejos por perro es ",cuotaminima)

#         for i in range(perros):
#                 conejos=random.randint(0,6)
#                 print("perro", i+1, "trajo", conejos)
#                 if cuotaminima<=conejos:
#                     print(f"el perro {i+1} cumplio la cuota")
#                     cumplen+=1
#                 else:
#                     print(f"el perro {i+1} no cumplio la cuota")           
#         print("el total de perros que cumplio ",cumplen)
#         print("el total de perros que no cumplieron",perros-cumplen)
#         break
#     except ValueError as exepcion:
#                 print("solo debes poner numeros enteros")     

###########################
###########################



# quieres pasar el ramo?
# pregunte la cantidad de rojos en el Curso 
# los talleres que hay en el semestre son 4 
# por cada taller asistido obtiene 0.3 decimas
# si el alumno tiene mas de 1 punto
# tiene la bedicion del profesor
# sino, no se le puede ayudar
# ingrese la nota final y sume las decimas acomuladas
# muestre si aprueba o reprueba


rojos=int(input("cuantos rojos tiene en el curso "))
talleres=4
decimas=0
while True:
    asis=int(input("asistió al taller 1? 1-Si 2-No "))
    if asis==1:
        decimas=decimas+0.3
    else:
        decimas=decimas+0    
    asis=int(input("asistió al taller 2? 1-Si 2-No "))
    if asis==1:
        decimas=decimas+0.3  
    else:
        decimas=decimas+0 
    asis=int(input("asistió al taller 3? 1-Si 2-No "))
    if asis==1:
        decimas=decimas+0.3  
    else:
        decimas=decimas+0 
    asis=int(input("asistió al taller 4? 1-Si 2-No "))
    if asis==1:
        decimas=decimas+0.3  
    else:
        decimas=decimas+0                
    break
print("sus decimas por los talleres son ",decimas)