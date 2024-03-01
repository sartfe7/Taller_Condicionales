# Programa para solicitar un prestamo

# Entrada

ingreso_mensual = int(input("Ingrese su ingreso mensual: "))


if ingreso_mensual > 945200:

    deuda = input("¿Tiene alguna otra deuda? (sí/no): ")
    
# Proceso y salida

    if deuda == "no":
        print("Felicidades, usted es elegible para un préstamo bancario.")
    else:
        print("Lo sentimos, no cumple con los requisitos para obtener un préstamo bancario.")
else:
    print("Lo sentimos, no cumple con los requisitos para obtener un préstamo bancario.")