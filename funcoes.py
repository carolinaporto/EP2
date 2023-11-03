def filtra(palavras, n):
    lista = []

    for palavra in palavras:
        if len(palavra) == n:
            low = palavra.lower()
            if not low in lista:
                lista.append(low)
    
    return lista

def inicializa(palavras):
    import random
    dic = {}

    dic['n'] = len(palavras[0])
    dic['tentativas'] = len(palavras[0])+1
    dic['especuladas'] = []
    dic['sorteada'] = random.choice(palavras)

    return dic

def inidica_posicao(sorteada, tentativa):
    lista = []

    if len(sorteada) == len(tentativa):
        for i in range(len(sorteada)):
            
            if tentativa[i] in sorteada:
                if sorteada[i] == tentativa[i]:
                    lista.append(0)
                else:
                    lista.append(1)
            
            else:
                lista.append(2)
                
    return lista
