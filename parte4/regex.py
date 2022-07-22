import re

email1 = 'meu numero é 1234-1234'
email2 = 'Fale comigo em 1234-1234 esse é meu telefone'
email3 = '1234-1234 é o meu celular'
email4 = 'lalalal 99854-7724 e o 92933999'

padrao = '[0-9]{4,5}[-]*[0-9]{4}'
#print(padrao,type(padrao))
retorno = re.findall(padrao,email4)
print(retorno)