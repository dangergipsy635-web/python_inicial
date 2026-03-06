import os, time, random
def lanzar_dados():
    return random.randrange(1,7)
while True:
    op = int(input("Elegi un numero del dado: "))
    if op >=1 and op <=6:
        os,system("cls")
        print(F"Elegiste el {op}")
        print("Lanzamos el dado")
        time.sleep(3)
        dado = lanzar_dados()
        print(F"Ha caido el {dado}")

        if dado == op :
            print("Buena suerte, haz ganado!!!")
        else:
            print("Haz perdido, vuelve a intentarlo!!!")
    else:
        print("Juegos terminado")
        break