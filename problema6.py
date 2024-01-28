# ingresar su edad
edad = int(input("Ingrese su edad: "))

# Calculamos el precio de la entrada
if edad < 4:
    precio = 0  # Menores de 4 años entran gratis
elif 4 <= edad <= 18:
    precio = 5  # Entre 4 y 18 años pagan $5
else:
    precio = 10  # Mayores de 18 años pagan $10

# mostrar el precio de la entrada
print(f"El precio de la entrada es: ${precio}")