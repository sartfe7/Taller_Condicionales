# Progrma para calcular el gasto de agua de una vivienda dado el número de m3 de agua gastados

# Entrada
Gasto_M3 = int(input("Digite el gasto de agua en su vivienda en 😁: " ) )

Cuota_fija= 10000

# Processing 

if Gasto_M3 < 50:
    Costo = 0 + Cuota_fija
elif Gasto_M3 < 200:
    Costo = Cuota_fija+((Gasto_M3-50) *2000) 

else: 
    Costo=10000+3000*(Gasto_M3-50) 

# Output

print ("El valor a pagar por el consumo del agua es:", Costo, )