#42
from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

cpf_um = '11927912407'
#print(cpf_um)

exemplo_cnpj = '35379838000112'
#cnpj = CNPJ()
documento = CpfCnpj(cpf_um,'cpf')
print(documento)