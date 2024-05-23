alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
key = 'PEDRONAVAJA'
text = "GYLKWQRVEBTPXDJRQDDVQNPHHGQGUWRNPPWHRGCONLJOHMÑCOXEEAVASIÑDOEQPETAPVHEOPEKRXYAEVRUHAÑVNRSIVPZBSXINLEWSMGBSHEEITVDEENSVR"
def vigenere_descifrar(texto_plano, clave, modulo):
    alfabeto = alphabet
    n = len(alfabeto)

    # Cifrado Vigenère
    def get_index(c):
        return alfabeto.index(c) if c in alfabeto else None

    texto_plano_indices = [get_index(c) for c in texto_plano]
    clave_indices = [get_index(c) for c in clave]

    texto_cifrado_indices = []
    for i, index in enumerate(texto_plano_indices):
        if index is not None:
            key_index = clave_indices[i % len(clave_indices)]
            texto_cifrado_indices.append((index - key_index) % n)
        else:
            texto_cifrado_indices.append(index)  # Mantener caracteres no soportados

    texto_cifrado = ''.join(alfabeto[i] if i is not None else texto_plano[idx]
                            for idx, i in enumerate(texto_cifrado_indices))
    return texto_cifrado


print(vigenere_descifrar(text, key,27))

