# practica con listas 
lista = []
def cargar_lista():
    v = input("Ingrese un valor: ")
    lista.append(v)

def imprimir_lista():
    print("Elementos de la lista")
    print(lista)

while True:
    print("Gestionar lista")
    opcion = input("1.Cargar\n2.Imprimir\no.Salir\nElige: ")

    if(opcion == "1"):
        cargar_lista()
    elif(opcion == "2"):
        imprimir_lista()
    elif(opcion == "0"):
        print("hasta NUNCA")
        break

    else:
        print("Donde ves esa opcion, tarado")