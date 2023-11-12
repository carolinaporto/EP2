import random
from termcolor import colored

# Inicio do jogo:
print(" =========================== \n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === ")
print("Comandos: desisto")

print(f"\n Regras:\n  - Dependendo do número de letras da palavra que você escolher advinhar, você terá n+1 tentativas para acertá-la.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {colored('Azul', 'blue', attrs = ['bold'])}   : a letra está na posição correta;\n    . {colored('Amarelo', 'yellow', attrs = ['bold'])}: a palavra tem a letra, mas está na posição errada;\n    . {colored('Cinza', 'grey', attrs = ['bold'])}: a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\nSorteando uma palavra...")

print("Já tenho uma palavra! Tente adivinhá-la!")