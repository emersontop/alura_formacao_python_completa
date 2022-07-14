#Menu de jogos

import ex001
import ex002

print('='*35)
print('Escolha o jogo que você quer!')
print('='*35)

print('''Digite:
    [2] - Para o jogo da forca
    [1] - Para o jogo da adivinhação''')

jogo = int(input('Qual você quer jogar? '))

if (jogo == 2):
    print('Você escolheu o jogo da forca!')
    jogar_ex002()
elif (jogo == 1):
    print('Você escolheu o jogo da adivinhação!')
    jogar_ex001()