#import requests
from acesso_cep import BuscarEndereco

cep = 55675000
obj_cep = BuscarEndereco(cep)

#r = requests.get('https://viacep.com.br/ws/01001000/json/')
#print(r.text)

bairro, cidade, uf = obj_cep.acessa_via_cep()

print(bairro, cidade, uf)