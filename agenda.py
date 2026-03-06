import os # opcional 

agenda = ("emergencias": "911", "bombero":"120")
def cargar_agenda():
    nombre = input("Ingrese nombre:  ")
    tel = input("Ingrese telefono: ")
    agenda(nombre) = tel


def ver_agenda():
    print(agenda)

while True:

    print("Agenda telefonica")
    op = input("1.Cargar\n2.Ver\n0.Salir")
    if op == "1":
        cargar_agenda()
        os.system("cls")
    elif op == "2":
        os.system("cls")
        ver_agenda()
    elif op == "0:
        break
    else:
        print("?")