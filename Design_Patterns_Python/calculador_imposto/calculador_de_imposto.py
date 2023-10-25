from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):

        imposto_caculado = imposto.calcula(orcamento)

        print(imposto_caculado)


if(__name__ == '__main__'):
    
    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adciona_item(Item('Item - 1', 50.0))
    orcamento.adciona_item(Item('Item - 2', 200.0))
    orcamento.adciona_item(Item('Item - 3', 250.0))


    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())