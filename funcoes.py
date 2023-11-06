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

# função que retorna a palavra digitada já colorida
def cor(sorteada, tentativa):
    lista = inidica_posicao(sorteada, tentativa)
    pal = []
    for c in tentativa:
        pal.append(c)

    i = 0
    for num in lista:
        if num == 0:
            pal[i] = f'\033[0;034m{pal[i]}\033[m'
            i += 1
        elif num == 1:
            pal[i] = f'\033[0;033m{pal[i]}\033[m'
            i += 1
        elif num == 2:
            pal[i] = f'\033[0;037m{pal[i]}\033[m'
            i += 1
    tentativa = (" ").join(pal)
    tentativa = tentativa.replace(" ","")
    return tentativa