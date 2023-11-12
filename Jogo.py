from termcolor import colored
from funcoes import *
from base import *

# Menu inicial:
print(" =========================== \n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === ")
print("\nPara desistir, digite: desisto")

print(f"\n Regras:\n  - Dependendo do número de letras (n) da palavra que você escolher advinhar, você terá {colored('n+1', 'red')} tentativas para acertá-la.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {colored('Azul', 'blue', attrs = ['bold'])}   : a letra está na posição correta;\n    . {colored('Amarelo', 'yellow', attrs = ['bold'])}: a palavra tem a letra, mas está na posição errada;\n    . {colored('Cinza', 'grey', attrs = ['bold'])}: a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\n")

# Loop maior do jogo
while True:
    n = int(input('Você quer adivinhar uma palavra com quantas letras? '))
    while n > 23:
        print('Número de letras inválido')
        n = int(input('Digite outro número (até 23):'))

    print("Já tenho uma palavra! Tente adivinhá-la!\n")

    # Iniciando o jogo
    base = filtra(palavras, n)
    jogo = inicializa(base)
    sorteada = jogo['sorteada']
    display = " "

    # Jogo
    while jogo['tentativas'] > 0:
        chute = input('Digite uma palavra: ')

    # Validação de entrada
        while True:

            # Desistência
            if chute == "Desisto" or chute == "desisto":
                certeza = input("Tem certeza que deseja desisir? (s/n) ")
                if certeza == "s":
                    print(f'{colored(f">>> Que deselegante desistir, a palavra era: {sorteada}", "cyan")}\n')
                    break
                else:
                    print(f"Você tem {jogo['tentativas']} tentativas\n")
                    chute = input('Digite outra palavra: ')
            
            # Valida a entrada
            if not chute in palavras and chute != 'desisto': # Palavra na base de palavras
                print(f'{colored("Palavra desconhecida", "green")}\nVocê tem {jogo["tentativas"]} tentativas\n')
                chute = input('Digite uma palavra conhecida: ')
            elif len(chute) != n and chute != 'desisto': # Palavra com o número certo de letras
                print(f'{colored(f"Apenas palavras de {n} letras", "magenta")}\nVocê tem {jogo["tentativas"]} tentativas\n')
                chute = input(f'Digite uma palavra com {n} letras: ')
            elif (chute in palavras) and len(chute) == n and chute != 'desisto':
                break

        # Desiste
        if chute == "Desisto" or chute == "desisto":
            break

        # Se palavra digitada é igual à palavra sorteada
        if chute == sorteada:
            display = layout(n, sorteada, chute, display)
            print(display)
            jogo['tentativas'] -= 1
            print(f"*** Parabéns! Você acertou em {n+1-jogo['tentativas']} tentativas!")
            
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

    # Mensagem de derrota
    if jogo['tentativas'] == 0 and chute != sorteada:
        print(f'{colored("Você perdeu!", "red")}\n')
        print(f'A palavra correta era: {sorteada}\n')
    
    # Jogar novamente
    dnv = input("Voce deseja jogar novamente? (s/n) ")
    if dnv == "n":
        print("\n\nAté a proxima!!!")
        break


