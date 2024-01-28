# ingresar el numero de juguetes comprados
payasos = int(input("Ingrese el número de payasos: "))
muñecas = int(input("Ingrese el número de muñecas: "))

# se calcula el peso total de los juguetes
peso_payaso_en_gramos = 112  
peso_muñeca_en_gramos = 75 

peso_total = (payasos * peso_payaso_en_gramos) + (muñecas * peso_muñeca_en_gramos)

# imprimimos el resultado
print(f"El peso total del paquete será de {peso_total} gramos.")