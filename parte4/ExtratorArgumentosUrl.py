

from cgitb import lookup


class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError('URL inválida!!!')

    @staticmethod
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def ExtrairArgumentos(self):
        indiceFinalModedaDestino = self.url.find('&',45)
        indiceInicialMoedaDestino = self.url.find('=',45) +1

        indiceInicialMoedaOrigem = self.url.find('=') +1
        indiceFinalMoedaOrigem = self.url.find('&')

        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedaDestino : indiceFinalModedaDestino]

        return moedaOrigem, moedaDestino
