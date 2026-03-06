num1 = int(input("Ingrese un numero inicial: "))
num2 = int(input("Ingrese otro numero limite: "))

print(f"Valores entre {num1} y {num2}")
for x in range(num1+1, num2):
    print( f"| {x} ", end = " ")
print("|", end="\n")