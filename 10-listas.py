lenguajes= ["python", "rubi", "php", "javascrip", "java"]
# recordar que todo comienza con indice 0
# los indices pueden ser numeros negativos para empezar desde el ultimo
print(lenguajes[-1])
print("------------------")
# para cambiar 1 valor de un listado
lenguajes[1] = "go"
print(lenguajes)
print("------------------")
# para seleccionar un rango de un listado
print(lenguajes[0:3])
print("------------------")
# para agregar un elemento a la lista al final 
lenguajes.append("juan")
print(lenguajes)
print("------------------")
# para inserta un elemento en un indice determinado
lenguajes.insert(7,"hola")
print(lenguajes)
print("------------------")
# mostrar indice del elemento
print(lenguajes.index(3))
print("------------------")
# recorrer lista
for lenguaje in lenguajes:
    print(lenguaje+1)
    print("-----------------")

