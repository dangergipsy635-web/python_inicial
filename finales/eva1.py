MONTOIRP = 80000000
sueldoMesual = 5000000

#Calcular el sueldo anual
sueldoAnual = sueldoAnual * 12

#Verificar si supera el monto estrabrecido
if sueldoAnual > MONTOIRP:
    print("Esta persona debe pagar impuestos")
else:
    print("La persona NO debe abonar impuestos")
