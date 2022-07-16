#jogo da forca 1:47:49

def jogar():
    print('='*35)
    print('Bem vindo ao jogo de forca')
    print('='*35)

    palavra_secreta = 'banana'
    letras_acertadas = ['_','_','_','_','_','_']

    enforcou = False
    acertou = False
    erros = 0

    #print para mostrar o tamanho da palavra
    print(letras_acertadas)

    #Condição do while não enforcou e não acertou
    while (not enforcou and not acertou ):

        chute = str(input('Qual letra? '))
        #O metodo .strip() remove espaços antes e depois
        chute = chute.strip()

        #verificando se a letra está na palavras

        if(chute in palavra_secreta):
            
            #Index garda a posição da letra
            index = 0
            for letra in palavra_secreta:
                #O metodo .upper deixa em maiúsculo, assim se o usuário digitar maiúsculo não tem problema.
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index = index +1
        else:
            erros = erros + 1
        
        enforcou = erros == 6
        print(letras_acertadas)

    print('Fim de jogo')

if(__name__ == '__main__'):
    jogar()