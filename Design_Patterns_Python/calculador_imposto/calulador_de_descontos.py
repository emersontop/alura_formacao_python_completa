from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhetos_reais, Sem_desconto

class Calculado_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhetos_reais(Sem_desconto())
        ).calcula(orcamento)
        return desconto    
    
if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adciona_item(Item('Item - 1', 100.0))
    orcamento.adciona_item(Item('Item - 2', 50.0))
    orcamento.adciona_item(Item('Item - 3', 100.0))

    calculador = Calculado_de_descontos()
    desconto_calculado = calculador.calcula(orcamento)

    print ('Desconto calculado',desconto_calculado)