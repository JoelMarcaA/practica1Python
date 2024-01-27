# ingresamos dos numeros
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# enseñar el menú y obtener la opción del usuario
print("\nMenú:\n1. Mostrar suma\n2. Mostrar resta\n3. Mostrar multiplicación")

opcion = input("Ingrese el número de la opción deseada (1, 2 o 3): ")

# realizar la operación según la opción elegida
if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de los dos números es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta (primer número menos segundo número) es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de los dos números es: {resultado}")
else:
    print("Opción inválida. Por favor, ingrese 1, 2 o 3.")
