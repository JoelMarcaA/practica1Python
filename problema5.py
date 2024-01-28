# ingresar la cantidad de shows musicales vistos
cantidad_shows = int(input("Ingrese el numero de show vistos: "))

# Verificar si ha visto más de 3 shows
if cantidad_shows > 3:
    resultsado = True
else:
    resultado = False

# imprimimos el resultado
print(f"¿Ha visto más de 3 shows musicales? {resultado}")