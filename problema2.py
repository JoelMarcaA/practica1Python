# se solicita la cantidad de dinero total del consumo
dinero_gastado = float(input("Ingrese el dinero total de consumo: $"))
porcentaje_propina = 15

# calculamos la propina
propina = (porcentaje_propina/100) * dinero_gastado

# imprimimos el resultado
print(f"Debería dejar ${propina:.2f} como propina.")
