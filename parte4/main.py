#1:15:00

from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
url2 = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=500"
argumentosurl = ExtratorArgumentosUrl(url)
argumentosurl2 = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentosurl.ExtrairArgumentos()
valor = argumentosurl.extrairValor()
print(moedaOrigem, moedaDestino, valor)
print(len(argumentosurl))
print(argumentosurl)
print(id(argumentosurl))
print(id(argumentosurl2))
print(argumentosurl == argumentosurl2)
#ExtratorArgumentosUrl.urlEhValida('a')
'''

string = 'bytebankbankbank'
stringNova = string.replace('bank','rodrigo',1)
print(stringNova)'''