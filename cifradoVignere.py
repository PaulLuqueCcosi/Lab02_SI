# 6 ALGORITMO--------------------------------
def generar_alfabeto(modulo):
    if modulo == 27:
        # Alfabeto español con ñ
        return 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    elif modulo == 191:
        # ASCII extendido
        return '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬\xad®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþ'
    else:
        raise ValueError("Módulo no soportado. Use 27 o 191.")

def limpiar_texto(texto, modulo):
    # Convertir a mayúsculas
    

    if modulo == 27:
        texto = texto.upper()
        # Eliminar espacios
        texto = texto.replace(' ', '')
        # Convertir letras con tildes a sin tildes
        acentos = {
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U',
            'Ä': 'A', 'Ë': 'E', 'Ï': 'I', 'Ö': 'O', 'Ü': 'U',
            'Â': 'A', 'Ê': 'E', 'Î': 'I', 'Ô': 'O', 'Û': 'U'
        }
        texto = ''.join(acentos.get(c, c) for c in texto)
        # Eliminar signos de puntuación
        texto = ''.join(c for c in texto if c.isalpha())
    elif modulo == 191:
        # Eliminar espacios
        texto = texto.replace(' ', '')
    else:
        raise ValueError("Módulo no soportado. Use 27 o 191.")

    return texto


def vigenere_cifrar(texto_plano, clave, modulo):
    
    alfabeto = generar_alfabeto(modulo)
    n = len(alfabeto)

    # Limpiar texto plano y clave
    texto_plano = limpiar_texto(texto_plano, modulo)
    clave = limpiar_texto(clave, modulo)
 

    def get_index(c):
        return alfabeto.index(c) if c in alfabeto else None

    texto_plano_indices = [get_index(c) for c in texto_plano]
    clave_indices = [get_index(c) for c in clave]

    texto_cifrado_indices = []
    for i, index in enumerate(texto_plano_indices):
        if index is not None:
            key_index = clave_indices[i % len(clave_indices)]
            texto_cifrado_indices.append((index + key_index) % n)
            #print(f"{i}: {index}", end=", ")
        else:
            texto_cifrado_indices.append(index)  # Mantener caracteres no soportados
            print("caracter no sorportado")

    texto_cifrado = ''.join(alfabeto[i] if i is not None else texto_plano[idx]
                            for idx, i in enumerate(texto_cifrado_indices))
    return texto_cifrado

def leer_archivo(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def guardar_archivo(contenido):
    with open("cifrado.txt", 'w', encoding='utf-8') as file:
        file.write(contenido)

if __name__ == "__main__":
    # Selección del módulo
    modulo = int(input("Seleccione el módulo (27 o 191): "))
    
    # Entrada de texto plano
    opcion_entrada = input("¿Desea ingresar el texto plano por archivo o interfaz? (1/2): ").strip()
    if opcion_entrada == '1':
        file_path = input("Ingrese la ruta del archivo de texto plano: ").strip()
        texto_plano = leer_archivo(file_path)
    else:
        texto_plano = input("Ingrese el texto plano: ").strip()
    
    # Entrada de clave
    clave = input("Ingrese la clave: ").strip()
    
    # Generar el texto cifrado
    #----------------------------------------------------------------
    #texto_plano = "La perfección se logra no cuando no hay nada más que añadir, sino cuando no hay nada más que quitar"
    #clave= "MEZCLADOR"
    #modulo= 191
    texto_cifrado = vigenere_cifrar(texto_plano, clave, modulo)
    
    # Guardar o mostrar el resultado
    opcion_salida = input("¿Desea guardar el texto cifrado en un archivo o mostrar en pantalla? (1/2): ").strip()
    if opcion_salida == '1':
        guardar_archivo(texto_cifrado)
        print("Texto cifrado guardado en 'cifrado.txt'")
    else:
        print("Texto cifrado:")
        print(texto_cifrado)


# 7 Uso del algoritmo -----------------------


# 8 Verificar el cypher


# 9 fercuencias


# 10 descifrado


# 11 Demostrar con el software de la pagina