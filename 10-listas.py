lenguajes= ["python", "rubi", "php", "javascrip", "java"]
# recordar que todo comienza con indice 0

# los indices pueden ser numeros negativos para empezar desde el ultimo
print(lenguajes[-1])
print("------------------")

# para cambiar 1 valor de un listado

# lenguajes[1] = "go"
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

print(lenguajes.index)
print("------------------")

# recorrer lista

for lenguaje in lenguajes:
    print(lenguaje)
    print("-----------------")

# paara agregar un elemento en una posicion determinada

# lenguajes.insert(3, "go")
# lenguajes.insert(0, "c")
print(lenguajes)
print("---------")

# para eliminar un elemento (tienes que escribir el elemento NO el indice)

lenguajes.remove("rubi")
print(lenguajes)
print("---------")

# para eliminar a traves del indice
lenguajes.pop()

# para limpiar el listado

# lenguajes.clear()

# para saber cuanto elementos contiene un listado
print (len(lenguajes))
print(lenguajes)
print("---------")

# para mostrar lista de manera ordenada menor a mayor

lenguajes.sort()
print(lenguajes)
print("---------")

#para mostrar lista de mayor a menor 

lenguajes.reverse()
print(lenguajes)
print("---------")

# para sumar numeros 
sum(lenguajes)
# 
max()
# 
min()

kilo=[
    [2,4]
    [3,8]
]
print([1][1])
 
# diccionarios son conjunto de pares de datos

dic={
    "nombre": "david",
    "numero": 32132132,
    "casado" : True 
} 
print(dic()) 
print(dic["nombre"]) 

for key, value in dic.items():
    print(key,value)


# ------------------------

frutas={
    "manzana": 1500,
    "frutilla": 1600,
    "durazno": 3800
}

print(frutas)
frutas={"pera": 1200}

print(frutas)
