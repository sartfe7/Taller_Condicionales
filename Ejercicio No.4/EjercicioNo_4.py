# Programa para calcular el índice de masa corporal de una persona

# Input
PESO= int(input("Porfavor ingrese su peso : "))
ALTURA = float(input("Porfavor ingrese su altura : "))

# Processing
IMC = PESO/ALTURA**2

if IMC < 16:
    RESULTADO ="criterio de ingreso en hospital"
elif IMC <= 17:
    RESULTADO = "infrapeso" 
elif IMC <= 18.5:
    RESULTADO = "bajo peso"
elif IMC <= 25:
    RESULTADO = "peso normal (saludable)"
elif IMC <= 30:
    RESULTADO = "sobrepeso(obesidad de grado I)"
elif IMC <= 35:
    RESULTADO = "sobrepeso crónico(obesidad de grado II)"
elif IMC <= 40:
    RESULTADO = "obesidad premórbida(obesidad de grado III)"
elif IMC > 40:
    RESULTADO = "obesidad mórbida(obesidad de grado IV)"

# Output

print("Su IMC es",IMC,"y su resultado es 😊",RESULTADO,)
