

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    #ess @property informa para o python que esse metodo nome é uma propriedade e não precisa do ()

    @property
    def nome(self):
        print('Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('Chamando setter nome()')
        self.__nome = nome