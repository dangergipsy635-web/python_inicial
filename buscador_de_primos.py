numero = 100000000
while True:
    numero += 1 
    es_primo=  True
    for x in range(2,int(numero/2)): #probar con la mitad de los valores
        if numero % x == 0:
            es_primo = False
            break # romper el ciclo inmediato

if es_primo:
    print(numero)