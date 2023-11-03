import random
#comando para cores: '\033[0;033m7\033[m'

# Colorindo o texto do início do jogo:
Azul = '\033[0;034mAzul\033[m'
Amarelo = '\033[0;033mAmarelo\033[m'
Cinza = '\033[0;037mCinza\033[m'
tentativas = '\033[0;031m6\033[m'

# Inicio do jogo:
print(" =========================== \n|                           |\n| Bem-vindo ao Insper Termo |\n|                           |\n ==== Design de Software === ")
print("Comandos: desisto")

print(f"\n Regras:\n  - Você tem {tentativas} tentativas para acertar uma palavra aleatória de 5 letras.\n  - A cada tentativa, a palavra testada terá suas letras coloridas conforme:\n    . {Azul}   : a letra está na posição correta;\n    . {Amarelo}: a palavra tem a letra, mas está na posição errada;\n    . {Cinza}: a palavra não tem a letra.\n  - Os acentos são ignorados;\n  - As palavras podem possuir letras repetidas.\n\nSorteando uma palavra...")

print("Já tenho uma palavra! Tente adivinhá-la!")