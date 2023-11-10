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
        while not chute in palavras or len(chute) != n:
            #Desistência
            if chute == "Desisto" or chute == "desisto":
                break
            
            if not chute in palavras: # Palavra na base de palavras
                print(f'Palavra desconhecida\nVocê tem {jogo["tentativas"]} tentativas\n')
            elif len(chute) != n: # Palavra com o número certo de letras
                print(f'Apenas palavras de {n} letras\nVocê tem {jogo["tentativas"]} tentativas\n')
            chute = input('Digite outra palavra: ')

        # Checa desistência
        if chute == "Desisto" or chute == "desisto":
            certeza = input("Tem certeza que deseja desisir? (s/n) ")
            if certeza == "s":
                print(f">>> Que deselegante desistir, a palavra era: {sorteada}\n")
                break
            else:
                print(f"Você tem {jogo['tentativas']} tentativas\n")
                chute = input('Digite outra palavra: ')

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


