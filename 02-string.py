texto = "hola mundo"
print(texto.upper())
print(texto.lower())
# busca los caracteres dados
print(texto.find("mun")) 
# reemplaza textos asignados pero no cambia la variable original
nuevotexto= texto.replace("mundo", "joni")
print(texto, nuevotexto)
# buscar palabra dentro de una variable 
print("mundo" in texto)