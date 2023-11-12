from termcolor import colored
import random

def filtra(palavras, n):
    lista = []

    for palavra in palavras:
        if len(palavra) == n:
            low = palavra.lower()
            if not low in lista:
                lista.append(low)
    
    return lista

def inicializa(palavras):
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

# função que retorna uma lista com as letras coloridas
def cor(sorteada, tentativa):
    lista = inidica_posicao(sorteada, tentativa)
    pal = []
    for c in tentativa:
        pal.append(c)

    i = 0
    for num in lista:
        if num == 0:
            pal[i] = colored(f'{pal[i]}', 'blue', attrs = ['bold'])
            i += 1
        elif num == 1:
            pal[i] = colored(f'{pal[i]}', 'yellow', attrs = ['bold'])
            i += 1
        elif num == 2:
            pal[i] = colored(f'{pal[i]}', 'grey', attrs = ['bold'])
            i += 1
    
    return pal

def layout(n, sorteada, tentativa, display):
    print(display)
    chute = cor(sorteada, tentativa)
    if display == " ":
        display += " ---"*n + "\n"

    for i in range(len(chute)):
        display +=  (" | " + str(chute[i]))
    display += " |\n "
    display += (" ---"*n + "\n")
    return display

