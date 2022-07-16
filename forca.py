#jogo da forca 1:47:49

#impotando a biblioteca random
import random

def imprime_mensagem_de_abertura():
    print('='*35)
    print('Bem vindo ao jogo de forca')
    print('='*35)


def carrega_palavra_secreta():
    #Abrindo o arquivo para leitura
    arquivo = open('palavras.txt','r')

    #criando uma lista para receber as palavras do arquivo
    palavras = []

    #fazendo um laço para ler cada linha do arquivo
    for linha in arquivo:
        #limpando a linha, retirando caracteres que não vamo usar
        linha = linha.strip()
        
        #adicionando ao final da minha lista (append()) cada palavras
        palavras.append(linha)

    #Fechamento do arquivo
    arquivo.close()

    #Escolnhendo aleatóriamente as palavras dentro do arquivo
    numero = random.randrange(0,len(palavras))


    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    lista = ['_' for letra in palavra_secreta]
    return lista


def pede_chute():
    chute = str(input('Qual letra? '))
    #O metodo .strip() remove espaços antes e depois
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    #Index garda a posição da letra
    index = 0
    for letra in palavra_secreta:
        #O metodo .upper deixa em maiúsculo, assim se o usuário digitar maiúsculo não tem problema.
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print('Parabéns, você ganhou! ')


def imprime_mensagem_perdedor():
    print('Você perdeu" : ( ')

def jogar():

    imprime_mensagem_de_abertura()

    palavra_secreta = carrega_palavra_secreta()
    
    #Prenche a lista letras_acertadas com '_' do tamanho da palavra!
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    #print para mostrar o tamanho da palavra
    print(letras_acertadas)

    #Condição do while não enforcou e não acertou
    while (not enforcou and not acertou ):

        chute = pede_chute()

        #verificando se a letra está na palavras
        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

if(__name__ == '__main__'):
    jogar()