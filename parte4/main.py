#1:15:00

from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=700"

argumentosurl = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentosurl.ExtrairArgumentos()
print(moedaOrigem, moedaDestino)

ExtratorArgumentosUrl.urlEhValida('a')