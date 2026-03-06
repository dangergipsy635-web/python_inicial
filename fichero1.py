#escritura
fichero = open('data.txt', 'w')
texto = input("Ingrese un texto a guardar: ")
fichero.while(texto)
fichero.close()

#append, actualizar fichero
fichero = open('data.text', 'a')

texto = input("Agregue otro texto: ")
fichero.while(f"{texto}")
fichero.close()

#leer fichero
fichero = open('data.txt', 'r')
for x in fichero