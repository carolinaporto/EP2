from funcoes import *
from base import words

while True:
    n = int(input('Você quer adivinhar uma palavra com quantas letras? '))

    base = filtra(words, n)
    jogo = inicializa(base)

    while jogo['tentativas'] > 0:
        sorteada = jogo['sorteada']
        chute = input('Digite uma palavra: ')

        # Checa se o usuario quer desistir
        if chute == "Desisto" or chute == "desisto":
            certeza = input("Tem certeza que deseja desisir? (s/n) ")
            if certeza == "s":
                print(f">>> Que deselegante desistir, a palavra era: {sorteada}\n")
                break
            else:
                print(f"Você tem {jogo['tentativas']} tentativas\n")
                chute = input('Digite outra palavra: ')
        
        #Checa palavra com numero de letras diferente
        while len(chute) != n:
            print(f'Apenas palavras de {n} letras\nVocê tem {jogo["tentativas"]} tentativas\n')
            chute = input('Digite outra palavra: ')

        #Checa palavra desconhecida
        while not chute in base:
            print(f'Palavra desconhecida\nVocê tem {jogo["tentativas"]} tentativas\n')
            chute = input('Digite outra palavra: ')
        
        
        #Se palavra digitada == palavra sorteada
        if chute == sorteada:
            print('Boa jenio')
            break
        else:
            print(cor(sorteada, chute))
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


