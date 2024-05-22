# 6 ALGORITMO--------------------------------
def generar_alfabeto(modulo):
    if modulo == 27:
        # Alfabeto español con ñ
        return 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    elif modulo == 191:
        # ASCII extendido
        return ''.join(chr(i) for i in range(32, 223))
    else:
        raise ValueError("Módulo no soportado. Use 27 o 191.")

def vigenere_cifrar(texto_plano, clave, modulo):
    alfabeto = generar_alfabeto(modulo)
    n = len(alfabeto)

    # Eliminar espacios del texto plano y clave
    texto_plano = texto_plano.replace(' ', '').upper()
    clave = clave.replace(' ', '').upper()
    
    def get_index(c):
        return alfabeto.index(c) if c in alfabeto else None

    texto_plano_indices = [get_index(c) for c in texto_plano]
    clave_indices = [get_index(c) for c in clave]

    texto_cifrado_indices = []
    for i, index in enumerate(texto_plano_indices):
        if index is not None:
            key_index = clave_indices[i % len(clave_indices)]
            texto_cifrado_indices.append((index + key_index) % n)
        else:
            texto_cifrado_indices.append(index)  # Mantener caracteres no soportados

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
    opcion_entrada = input("¿Desea ingresar el texto plano por archivo o interfaz? (1/2): ").strip().lower()
    if opcion_entrada == 1:
        file_path = input("Ingrese la ruta del archivo de texto plano: ").strip()
        texto_plano = leer_archivo(file_path)
    else:
        texto_plano = input("Ingrese el texto plano: ").strip().upper()
    
    # Entrada de clave
    clave = input("Ingrese la clave: ").strip().upper()
    
    # Generar el texto cifrado
    texto_cifrado = vigenere_cifrar(texto_plano, clave, modulo)
    
    # Guardar o mostrar el resultado
    opcion_salida = input("¿Desea guardar el texto cifrado en un archivo o mostrar en pantalla? (1/2): ").strip().lower()
    if opcion_salida == '1':
        guardar_archivo( texto_cifrado)
        print(f"Texto cifrado guardado en cifrado.txt")
    else:
        print("Texto cifrado:")
        print(texto_cifrado)

# 7 Uso del algoritmo -----------------------


# 8 Verificar el cypher


# 9 fercuencias


# 10 descifrado


# 11 Demostrar con el software de la pagina