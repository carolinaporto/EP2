import random
from termcolor import colored
from funcoes import *
from base import *

# Inicio do jogo:
print(" =========================== \n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === ")
print("Comandos: desisto")

print(f"\n Regras:\n  - Dependendo do número de letras (n) da palavra que você escolher advinhar, você terá {colored('n+1', 'red')} tentativas para acertá-la.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {colored('Azul', 'blue', attrs = ['bold'])}   : a letra está na posição correta;\n    . {colored('Amarelo', 'yellow', attrs = ['bold'])}: a palavra tem a letra, mas está na posição errada;\n    . {colored('Cinza', 'grey', attrs = ['bold'])}: a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\n")

while True:
    n = int(input('Você quer adivinhar uma palavra com quantas letras? '))
    print("\nSorteando uma palavra... \nJá tenho uma palavra! Tente adivinhá-la!\n")

    display = " "

    base = filtra(words, n)
    jogo = inicializa(base)

    while jogo['tentativas'] > 0:
        sorteada = jogo['sorteada']
        chute = input('Digite uma palavra: ')

        # Enquanto as condições de jogo não são apropriadas:
        while (chute == "Desisto" or chute == "desisto") or (len(chute) != n) or (chute not in base):
             # Checa se o usuario quer desistir
            if (chute == "Desisto" or chute == "desisto"):
                certeza = input("Tem certeza que deseja desisir? (s/n) ")
                if certeza == "s":
                    print(f">>> Que deselegante desistir, a palavra era: {sorteada}\n")
                    break
                else:
                    print(f"Você tem {jogo['tentativas']} tentativas\n")
                    chute = input('Digite outra palavra: ')
        
            #Checa numero de letras das palavras:
            if len(chute) != n:
                print(f"\nApenas palavras de {n} letras\nVocê tem {jogo['tentativas']} tentativas\n")
                chute = input('Digite outra palavra: ')

            #Checa palavra desconhecida:
            if not chute in base:
                print(f'\nPalavra desconhecida\nVocê tem {jogo["tentativas"]} tentativas\n')
                chute = input('Digite outra palavra: ')
        

        #Se palavra digitada é igual à palavra sorteada
        if chute == sorteada:
            display = layout(n, sorteada, chute, display)
            print(display)

            jogo['tentativas'] -= 1
            print(f"*** Parabéns! Você acertou após {n+1-jogo['tentativas']} tentativas!")
            break
        else:
            display = layout(n, sorteada, chute, display)
            print(display)

            jogo['tentativas'] -= 1
            tentativas = jogo['tentativas']
            if tentativas > 1:
                print(f'Você tem {tentativas} tentativas restantes')
            elif tentativas == 1:
                print(f'Você tem {tentativas} tentativa restantes')

    if tentativas == 0:
        print('Você perdeu')
        print(f'A palavra correta era {sorteada}')
    
    dnv = input("Voce deseja jogar novamente? (s/n) ")
    if dnv == "n":
        print("\n\n\nAte a proxima!!!")
        break


