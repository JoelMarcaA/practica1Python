# ingrese la hora en formato de 24 horas
hora_ingresada = input("Ingrese la hora (por ejemplo, 01:30): ")

# extraemos las horas y minutos
try:
    horas, minutos = map(int, hora_ingresada.split(':'))
except ValueError:
    print("Formato de hora incorrecto. Por favor, ingrese la hora en formato de 24 horas.")
    exit()
    
# se determina si es hora de comer
if 7 <= horas <= 8 or 12 <= horas <= 13 or 18 <= horas <= 19:
    if 7 <= horas <= 8:
        print("¡Es hora de desayunar!")
    elif 12 <= horas <= 13:
        print("¡Es hora de almorzar!")
    else:
        print("¡Es hora de cenar!")
else:
    print("No es hora de comer en este momento.")