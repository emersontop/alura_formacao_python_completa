import sys
import os

# Obtém o caminho absoluto para o diretório raiz do projeto
projeto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(projeto_dir)

from calculador_imposto.calulador_de_descontos import Calculado_de_descontos
from calculador_imposto.orcamento import Orcamento, Item

def test_deve_retornar_valor_do_desconto_por_compras_de_mais_de_5_items():
    orcamento = Orcamento()
    orcamento.adciona_item(Item('Item - 1', 50.0))
    orcamento.adciona_item(Item('Item - 1', 50.0))
    orcamento.adciona_item(Item('Item - 1', 50.0))
    orcamento.adciona_item(Item('Item - 1', 50.0))
    orcamento.adciona_item(Item('Item - 1', 50.0))
    orcamento.adciona_item(Item('Item - 1', 50.0))

    calculador = Calculado_de_descontos()
    desconto_calculado = calculador.calcula(orcamento)

    assert desconto_calculado == (30) 