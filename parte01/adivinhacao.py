#Jogo de adivinhação

import random

def jogar():

    print('='*35)
    print('Bem vindo ao jogo de adivinhação')
    print('='*35)

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print('Qual nivel de dificuldade você deseja?')
    print('''Digite:
        [1] para fácil
        [2] para médio
        [3] difícil''')
    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5


    for rodada in range(1,total_de_tentativas + 1):
        print('tentativa {} de {}'.format(rodada,total_de_tentativas))

        chute_str = input('Digite o seu número entre 0 e 100: ')
        print('Você digitou! ',chute_str)
        chute_int = int(chute_str)

        if(chute_int<1 or chute_int>100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            if(maior):
                print('Você errou! Digite um numero menor')
            elif(menor):
                print('Você errou! Digite um nuemro maior')
        pontos_perdidos = abs(numero_secreto - chute_int)
        pontos = pontos - pontos_perdidos

    print('Fim de jogo')
if(__name__ == '__main__'):
    jogar()