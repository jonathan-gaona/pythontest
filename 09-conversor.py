temperatura = float(input("ingrese temperatura"))
escala = input("Es fahrenheit(F) o Es celsius (C)?:").lower()

if escala == "f":
    celsius= (temperatura - 32) * 5/9
    print(celsius)
elif escala == "c":
    fahrenheit= temperatura * 1.8 + 32
    print(fahrenheit)
else:
    print("escala incorrecta")