 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2:
    print(f"{num1} es mayor")
    if num1 % 2 == 0:
            print("es par")
    else:
            print("es impar")
elif num1 < num2:    
      print("{num2} es mayor a {num1}")
else:  
    print("Ambos numeros son iguales")