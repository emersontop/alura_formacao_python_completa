#Jogo de adivinhação

print('='*35)
print('Bem vindo ao jogo de adivinhação')
print('='*35)

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

for rodada in range(1,total_de_tentativas + 1):
    print('tentativa {} de {}'.format(rodada,total_de_tentativas))
    chute_str = input('Digite o seu número: ')
    print('Você digitou! ')
    chute_int = int(chute_str)

    acertou = chute_int == numero_secreto
    maior = chute_int > numero_secreto
    menor = chute_int < numero_secreto

    if(acertou):
        print('Você acertou! ')
        break
    else:
        if(maior):
            print('Você errou! Digite um numero menor')
        elif(menor):
            print('Você errou! Digite um nuemro maior')

print('Fim de jogo')