def leer_linea(archivo):
    """Leer una línea del archivo hasta el siguiente salto de línea"""
    with open(archivo, 'r') as f:
        return f.readline()


def inicializar_frecuencias():
    """Inicializar el diccionario de frecuencias con las letras de 'A' a 'Z'"""
    frecuencias = {}
    for i in range(65, 91):  # ASCII values for 'A' to 'Z'
        frecuencias[chr(i)] = 0
    return frecuencias

def contar_frecuencias(linea, frecuencias):
    """Contar las frecuencias de cada letra en la línea"""
    for char in linea:
        if 'A' <= char <= 'Z':
            if char in frecuencias:
                frecuencias[char] += 1
            else:
                frecuencias[char] = 1
    return frecuencias

def cinco_mas_frecuentes(frecuencias):
    """Encontrar las cinco letras con mayor frecuencia"""
    items = list(frecuencias.items())
    # Ordenar manualmente usando bubble sort (simple pero no eficiente)
    for i in range(len(items)):
        for j in range(len(items) - i - 1):
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    return items[:5]

def frecuencias(archivo):
    """Función principal que coordina todas las etapas y devuelve el diccionario de frecuencias"""
    # Leer una línea del archivo
    linea = leer_linea(archivo)
    
    # Inicializar el diccionario de frecuencias
    frecuencias_dict = inicializar_frecuencias()
    
    # Contar las frecuencias de cada letra en la línea
    frecuencias_dict = contar_frecuencias(linea, frecuencias_dict)
    
    # Encontrar las cinco letras con mayor frecuencia
    cinco_frecuentes = cinco_mas_frecuentes(frecuencias_dict)
    
    # Imprimir las cinco letras más frecuentes
    print("Cinco caracteres de mayor frecuencia:")
    for letra, freq in cinco_frecuentes:
        print(f"{letra}: {freq}")

    return frecuencias_dict

# Llamar a la función con el nombre del archivo
# Asegúrate de reemplazar 'archivo.txt' con la ruta de tu archivo
frecuencias_resultado = frecuencias('PRACTICA1_MEZ.TXT')
print(frecuencias_resultado)
print("###############################")
frecuencias_resultado = frecuencias('PRACTICA1_MALE.TXT')
print(frecuencias_resultado)
print("###############################")
frecuencias_resultado = frecuencias('PRACTICA1_QUESO.TXT')
print(frecuencias_resultado)
print("###############################")
frecuencias_resultado = frecuencias('PRACTICA1_MIA.TXT')
print(frecuencias_resultado)