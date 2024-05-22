MinusMayus = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E",
    "f": "F",
    "g": "G",
    "h": "H",
    "i": "I",
    "j": "J",
    "k": "K",
    "l": "L",
    "m": "M",
    "n": "N",
    "ñ": "Ñ",
    "o": "O",
    "p": "P",
    "q": "Q",
    "r": "R",
    "s": "S",
    "t": "T",
    "u": "U",
    "v": "V",
    "w": "W",
    "x": "X",
    "y": "Y",
    "z": "Z",
}

conversion_sintildes = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "Á": "A",
    "É": "E",
    "Í": "I",
    "Ó": "O",
    "Ú": "U",
    "ü": "u",
    "Ü": "U",
}


def aMayuscula(texto):

    texto_mayusculas = ""
    for char in texto:
        if char in MinusMayus:
            texto_mayusculas += MinusMayus[char]
        else:
            texto_mayusculas += char
    return texto_mayusculas


# Invertir el diccionario MinusMayus para crear MayusMinus
MayusMinus = {v: k for k, v in MinusMayus.items()}

def aMinus(texto):
    texto_minusculas = ""
    for char in texto:
        if char in MayusMinus:
            texto_minusculas += MayusMinus[char]
        else:
            texto_minusculas += char
    return texto_minusculas

def eliminar_tildes(texto):
    texto_sin_tildes = ""
    for char in texto:
        if char in conversion_sintildes:
            texto_sin_tildes += conversion_sintildes[char]
        else:
            texto_sin_tildes += char
    return texto_sin_tildes