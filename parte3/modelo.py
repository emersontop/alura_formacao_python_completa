#parada bloco4 1:05:10

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    def dar_like(self):
        self._likes +=1

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print('{} - {} - {}'.format(self._nome, self.ano, self._likes))

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} - {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} - {self.temporadas}'

class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)