cadena = input("Ingrese una oración: ")
longCad = len(cadena)
vocales = 0

for i in range(longCad):
    if cadena[i].lower() in "aeiou":
        vocales += 1

print("La oración ingresada es:", cadena)
print("La cantidad de vocales es:", vocales)
