PI = 3.14

def menu():
    print("1. Calcular area Triangulo")
    print("1. Calcular primetro Triangulo")
    op= input("Opcion: ")
    return op

def getAreaTriangulo(base, altura):
    return(base * altura) /2

def getPerimetroTriangulo(lado1 , lado2, lado3):
    return lado1 + lado2 + lado3

def getAreaRectangulo(largo,ancho):
    return largo * ancho

def getPerimetroRectangulo(largo, ancho):
    return(largo + ancho) * 2

def getAreaElipse(radio, excentricidad = 1):
    pass

def getPerimetroElipse(radio):
    return 2 * PI * radio

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1":
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            resultado = getAreaTriangulo(base, altura)
            print(f"El area es {resultado} u2")

        elif opcion == "2":
            l1 = float(input("lado 1: "))
            l2 = float(input("lado 2: "))
            l3 = float(input("lado 3: "))
            resultado = getPerimetroTriangulo(l1,l2,l3)
            print(f"El perimetro es {resultado} u ")