class Orcamento(object):

    def __init__(self, valor):
        self.__valor = valor
    
    @property
    def valor(self):
        #propert, ele retorna os valores qeu não podem ser acessados
        return self.__valor
