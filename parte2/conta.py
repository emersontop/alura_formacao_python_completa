

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Contruindo objeto ... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)