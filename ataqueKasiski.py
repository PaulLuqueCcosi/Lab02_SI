# Algoritmo con el ataque.

# MCD
def calcular_mcd_de_dos(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcd_lista(numeros):
    if not numeros:
        return None  # O podrías lanzar una excepción o retornar un valor predeterminado
    mcd = numeros[0]
    for numero in numeros[1:]:
        mcd = calcular_mcd_de_dos(mcd, numero)
        if mcd == 1:  # Si en algún punto el MCD es 1, no es necesario seguir
            break
    return mcd

import math
from functools import reduce

def mcd_lista(numeros):
    return reduce(math.gcd, numeros)

# primero tenemos que tener determinar las repeticiones de los trigramas
def leer_contenido(archivo):
    """Leer una línea del archivo hasta el siguiente salto de línea"""
    with open(archivo, 'r',  encoding="utf-8") as f:
        return f.readline()


def encontrar_trigramas(contenido, n):
    """Encontrar n-gramas en el contenido y sus posiciones"""
    n_gramas = {}
    for i in range(len(contenido) - n + 1):
        n_grama = contenido[i:i+n]
        if n_grama in n_gramas:
            n_gramas[n_grama].append(i)
        else:
            n_gramas[n_grama] = [i]
    return n_gramas

def calcular_distancias(trigramas):
    """Calcula las distancias entre trigramas consecutivos."""
    # Crea un diccionario para almacenar las distancias entre trigramas.
    distancias = {}
    
    # Itera sobre cada trígrama y sus posiciones en el texto.
    for trigrama, posiciones in trigramas.items():
        # Verifica si hay más de una posición para el trígrama.
        if len(posiciones) > 1:
            # Si hay más de una posición, inicializa una lista para almacenar las distancias.
            distancias[trigrama] = []
            
            # Itera sobre las posiciones del trígrama.
            for j in range(1, len(posiciones)):
                # Calcula la distancia entre posiciones consecutivas del trígrama.
                distancia = posiciones[j] - posiciones[j - 1]
                
                # Agrega la distancia calculada a la lista de distancias para este trígrama.
                distancias[trigrama].append(distancia)
    
    # Devuelve el diccionario de distancias calculadas.
    return distancias


def distancia_trigramas_consecutivos(archivo):
    """Función principal para implementar el método Kasiski"""
    # Leer el contenido del archivo
    contenido = leer_contenido(archivo)
    
    # Encontrar los trigramas y sus posiciones
    trigramas = encontrar_trigramas(contenido, 4)
    
    # Calcular las distancias entre trigramas consecutivos
    distancias = calcular_distancias(trigramas)
    
    # Filtrar solo trigramas que tienen distancias calculadas
    distancias = {trigrama: dist for trigrama, dist in distancias.items() if dist}
    
    array_trigramas = list(distancias.values())
    array_trigramas = [item for sublist in array_trigramas for item in sublist]

    # CALCULO DE mcd
    mcdNumeros = calcular_mcd_lista(array_trigramas)

    
    # Imprimir los resultados
    print("Trigramas y sus distancias:")
    for trigrama, dist in distancias.items():
        print(f"{trigrama}: {dist}")
    
    
    print(f"Arary con las posiciones {array_trigramas}")
    print(mcdNumeros)
    
    return distancias


def generar_subcriptogramas(criptograma, longitud_clave):
    subcriptogramas = ['' for _ in range(longitud_clave)]
    
    for i, caracter in enumerate(criptograma):
        subcriptogramas[i % longitud_clave] += caracter
        
    return subcriptogramas

def guardar_subcriptogramas(subcriptogramas, prefijo_archivo='subcriptograma'):
    for i, subcriptograma in enumerate(subcriptogramas):
        nombre_archivo = f"{prefijo_archivo}_{i+1}.txt"
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(subcriptograma)
        print(f"Subcriptograma {i+1} guardado en {nombre_archivo}")
        
# # Llamar a la función con el nombre del archivo
# distancias_resultado = distancia_trigramas_consecutivos('CRIPTO.TXT')
# Nombre del archivo que contiene el criptograma
nombre_archivo = 'CRIPTO.TXT'
longitud_clave = 7

# Leer criptograma
criptograma = leer_contenido(nombre_archivo)

# Generar subcriptogramas
subcriptogramas = generar_subcriptogramas(criptograma, longitud_clave)
guardar_subcriptogramas(subcriptogramas)

print(subcriptogramas)
