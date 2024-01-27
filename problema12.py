# colocar el nombre del archivo
archivo = input("Ingrese el nombre del archivo: ")

# verificar la extensión del archivo
if '.' in archivo:
    extension = archivo.split('.')[-1].lower()
else:
    extension = ""

# Definir el diccionario de tipos MIME
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip'}

# obtener el tipo MIME correspondiente
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

# imprimir el resultado
print(f"Tipo MIME para {archivo}: {tipo_mime}")
