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
        self._programas = programas

    def __getitem__(self,item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme('Vingadores - Guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
todo_mundo_em_panico = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_like()
todo_mundo_em_panico.dar_like()
todo_mundo_em_panico.dar_like()
todo_mundo_em_panico.dar_like()
atlanta.dar_like()
demolidor.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, todo_mundo_em_panico]

playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'tamanho da minha lista {len(playlist_fim_de_semana)}')

print(f'tá ou nun ta? {vingadores in playlist_fim_de_semana}')

for programa in playlist_fim_de_semana:
    print(programa)