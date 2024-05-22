import utils

# 1 ALGORITMO--------------------------------
# Definición del alfabeto de módulo 27
ALFABETO = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
ESPACIO_TO = ""
def limpiar_caracteres(texto_plano, alfabeto=ALFABETO, espacio=ESPACIO_TO):
    texto_limpio = ''
    for caracter in texto_plano:
        if caracter in ALFABETO:
            texto_limpio += caracter
        elif caracter == " ":
            texto_limpio += espacio
    return texto_limpio

def preprocesado(texto):
    # print(texto)
    texto_sin_tildes = utils.eliminar_tildes(texto)
    # print(texto_sin_tildes)
    texto_mayus = utils.aMayuscula(texto_sin_tildes)
    # print(texto_mayus)
    texto_limpio = limpiar_caracteres(texto_mayus)
    # print(texto_limpio)
    return texto_limpio
    
                               
def cifrar_texto(texto_claro, desplazamiento):
    texto_preprocesado = preprocesado(texto_claro)
    texto_cifrado = ''
    for caracter in texto_preprocesado:
        if caracter in ALFABETO:
            indice_original = ALFABETO.index(caracter)
            indice_cifrado = (indice_original + desplazamiento) % 27
            texto_cifrado += ALFABETO[indice_cifrado]
        else:
            texto_cifrado += caracter  # Para caracteres no incluidos en el alfabeto
    return texto_cifrado



def interfaz_usuario_cifrado():

    texto_claro = input("Ingrese el texto claro: ").strip()
    desplazamiento = int(input("Desplazamiento: "))
        
    texto_resultante = cifrar_texto(texto_claro, desplazamiento)
    print("Texto cifrado:", texto_resultante)


# 2 Uso del algoritmo -----------------------


# 4 Verificar el cypher


# 5 Algoritmo de descrifrado


## app

    
if __name__ == "__main__":
    menu = {
        "1" : "Cifrado cesar",
    }
    
    for key, val in menu.items():
        print(f"Opcion {key}: {val}")
    
    if(input() == "1"):
        interfaz_usuario_cifrado()