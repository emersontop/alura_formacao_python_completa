import sys
import os

# Obtém o caminho absoluto para o diretório raiz do projeto
projeto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(projeto_dir)

from leilao.dominio import Usuario, Leilao
from leilao.excecoes import LanceInvalido
import pytest

@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subitratir_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def teste_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0

def teste_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0

def teste_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 200.0)