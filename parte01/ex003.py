#Menu de jogos

import forca
import adivinhacao

def escolhe_jogo():

    print('='*35)
    print('Escolha o jogo que você quer!')
    print('='*35)

    print('''Digite:
        [2] - Para o jogo da forca
        [1] - Para o jogo da adivinhação''')

    jogo = int(input('Qual você quer jogar? '))

    if (jogo == 2):
        print('Você escolheu o jogo da forca!')
        forca.jogar()
    elif (jogo == 1):
        print('Você escolheu o jogo da adivinhação!')
        adivinhacao.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()

#min 25 bloco 02