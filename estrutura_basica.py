from funcoes import *
from base import *

while True:
    n = int(input('Você quer adivinhar uma palavra com quantas letras? '))
    while n > 23:
        print('Número de letras inválido')
        n = int(input('Digite outro número (até 23):'))
    
    # Iniciando o jogo
    base = filtra(palavras, n)
    jogo = inicializa(base)
    sorteada = jogo['sorteada']

    # Jogo
    while jogo['tentativas'] > 0:
        chute = input('Digite uma palavra: ')
        
    # Validação de entrada
        while True:
            #Desistência
            if chute == "Desisto" or chute == "desisto":
                certeza = input("Tem certeza que deseja desisir? (s/n) ")
                if certeza == "s":
                    print(f">>> Que deselegante desistir, a palavra era: {sorteada}\n")
                    break
                else:
                    print(f"Você tem {jogo['tentativas']} tentativas\n")
                    chute = input('Digite outra palavra: ')
            
            if not chute in palavras and chute != 'desisto': # Palavra na base de palavras
                print(f'Palavra desconhecida\nVocê tem {jogo["tentativas"]} tentativas\n')
                chute = input('Digite uma palavra conhecida: ')
            elif len(chute) != n and chute != 'desisto': # Palavra com o número certo de letras
                print(f'Apenas palavras de {n} letras\nVocê tem {jogo["tentativas"]} tentativas\n')
                chute = input(f'Digite uma palavra com {n} letras: ')
            elif (chute in palavras) and len(chute) == n and chute != 'desisto':
                break

        # Desiste
        if chute == "Desisto" or chute == "desisto":
            break

        # Se palavra digitada == palavra sorteada
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

    # Mensagem de derrota
    if jogo['tentativas'] == 0:
        print('Você perdeu')
        print(f'A palavra correta era {sorteada}')
    
    # Jogar novamente
    dnv = input("Voce deseja jogar novamente? (s/n) ")
    if dnv == "n":
        print("\n\nAte a proxima!!!")
        break


