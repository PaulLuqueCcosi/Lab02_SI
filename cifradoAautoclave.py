# 12 Algortimo Descrifrar
alfabeto ='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
def autoclave_descifrar(texto_cifrado, clave):
    
    n = len(alfabeto)

    def get_index(c):
        return alfabeto.index(c) if c in alfabeto else None

    texto_cifrado_indices = [get_index(c) for c in texto_cifrado]
    clave_indices = [get_index(c) for c in clave]

    texto_plano_indices = []
    for i in range(len(texto_cifrado_indices)):
        if i < len(clave_indices):
            key_index = clave_indices[i]
        else:
            key_index = texto_plano_indices[i - len(clave_indices)]
        index = (texto_cifrado_indices[i] - key_index) % n
        texto_plano_indices.append(index)

    texto_plano = ''.join(alfabeto[i] for i in texto_plano_indices)
    return texto_plano
txt = "XHGDQESDMPKÑDEEDKNGJZPFJSUIFZOLFCINFJCESVZTGBFXCIUDAYNUUDIZYWWZBEYNVQWIVUNKZEPHDODQUZZLBDNDRWTHQSERÑIVMLERCMGIFLSORZXTSDIGLOXQSDJHWVCIWQXQJCKMBPOKMPSKMUVIMNJDNBLCSZHXHNYYUIXDBSOXHZLXWVGDJGXHWLTDWKÑSAQIMZLNBVMLXHUOQQXIQGWGUFTWKZKMOKUDNINSIFJDUOZIJBSVVOWFAIEÑGYOWPSOAP"
k = 'UNODELOSMASGRANDESCRIPTOGRAFOS'
print(autoclave_descifrar(txt, k))