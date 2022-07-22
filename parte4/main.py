#1:15:00

from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentosurl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentosurl.ExtrairArgumentos()
valor = argumentosurl.extrairValor()
print(moedaOrigem, moedaDestino, valor)

#ExtratorArgumentosUrl.urlEhValida('a')
'''

string = 'bytebankbankbank'
stringNova = string.replace('bank','rodrigo',1)
print(stringNova)'''