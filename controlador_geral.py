from indices import IndiceGeral
from chaves_primarias.filme import Filme
from chaves_secundarias.ano import Ano
from chaves_secundarias.genero import Genero
from chaves_secundarias.nacionalidade import Nacionalidade
from tela_geral import TelaGeral


class ControladorGeral:

    def __init__(self):
        self.__multilista = IndiceGeral()
        self.__tela = TelaGeral()

    @property
    def multilista(self):
        return self.__multilista

    @property
    def tela(self):
        return self.__tela

    #### ESSE MÉTODO VAI CHAMAR OS MÉTODOS DE ADIÇÃO DOS 4 TIPOS DE LISTAS PARA ENCADEAR O NOVO ELEMENTO EM CADA UMA DAS CATEGORIAS
    def adiciona_elemento(self):
        nome, ano, genero, nacionalidade = self.tela.adiciona_filme()
        filme = Filme(nome, ano, genero, nacionalidade)
        self.adiciona_lista_geral(filme)
        self.adiciona_lista_ano(filme)
        self.adiciona_lista_genero(filme)
        self.adiciona_lista_nacionalidade(filme)

    #### ESSE MÉTODO ADICIONA NOVOS ELEMENTOS NO FINAL DA LISTA (AQUI SE TRATA DA LISTA GERAL, DE TODOS OS ELEMENTOS)
    def adiciona_lista_geral(self, filme: Filme):
        if self.multilista.primeiro_geral is None:
            self.multilista.primeiro_geral = filme
            return
        lista_geral = self.multilista.primeiro_geral
        while lista_geral.proximo:
            lista_geral = lista_geral.proximo
        lista_geral.proximo = filme

    #### OS PRÓXIMOS DOIS MÉTODOS SE REFEREM A ADIÇÃO DE VALORES NO DIRETÓRIO "Ano" E SERVIRÁ DE MOLDE PARA "Gênero" E "Nacionalidade"
    def adiciona_lista_ano(self, filme: Filme):
        lista_ano = self.multilista.primeiro_ano
        if lista_ano is None:
            self.multilista.primeiro_ano = Ano(filme.ano, filme)
            return
        while True:
            if filme.ano == lista_ano.ano:
                self.adiciona_ano(filme, lista_ano)
                return
            if lista_ano.prox_ano is None:
                lista_ano.prox_ano = Ano(filme.ano, filme)
                return
            lista_ano = lista_ano.prox_ano

    def adiciona_ano(self, filme: Filme, lista_ano: Ano):
        lista_filmes_ano = lista_ano.primeiro
        while lista_filmes_ano.prox_ano:
            lista_filmes_ano = lista_filmes_ano.prox_ano
        lista_filmes_ano.prox_ano = filme
        lista_ano.quantidade += 1

    #### OS PRÓXIMOS DOIS MÉTODOS ADICIONAM NOVOS VALORES NO DIRETÓRIO DE "Gênero"
    def adiciona_lista_genero(self, filme: Filme):
        lista_genero = self.multilista.primeiro_genero
        if lista_genero is None:
            self.multilista.primeiro_genero = Genero(filme.genero, filme)
            return
        while True:
            if filme.genero == lista_genero.genero:
                self.adiciona_genero(filme, lista_genero)
                return
            if lista_genero.prox_genero is None:
                lista_genero.prox_genero = Genero(filme.genero, filme)
                return
            lista_genero = lista_genero.prox_genero

    def adiciona_genero(self, filme: Filme, lista_genero: Genero):
        lista_filmes_genero = lista_genero.primeiro
        while lista_filmes_genero.prox_genero:
            lista_filmes_genero = lista_filmes_genero.prox_genero
        lista_filmes_genero.prox_genero = filme
        lista_genero.quantidade += 1

    #### OS PRÓXIMOS DOIS MÉTODOS ADICIONAM NOVOS VALORES NO DIRETÓRIO DE "Nacionalidade"
    def adiciona_lista_nacionalidade(self, filme: Filme):
        lista_nacionalidade = self.multilista.primeiro_nacionalidade
        if lista_nacionalidade is None:
            self.multilista.primeiro_nacionalidade = Nacionalidade(filme.nacionalidade, filme)
            return
        while True:
            if filme.nacionalidade == lista_nacionalidade.nacionalidade:
                self.adiciona_nacionalidade(filme, lista_nacionalidade)
                return
            if lista_nacionalidade.prox_nacionalidade is None:
                lista_nacionalidade.prox_nacionalidade = Nacionalidade(filme.nacionalidade, filme)
                return
            lista_nacionalidade = lista_nacionalidade.prox_nacionalidade

    def adiciona_nacionalidade(self, filme: Filme, lista_nacionalidade: Nacionalidade):
        lista_filmes_nacionalidade = lista_nacionalidade.primeiro
        while lista_filmes_nacionalidade.prox_nacionalidade:
            lista_filmes_nacionalidade = lista_filmes_nacionalidade.prox_nacionalidade
        lista_filmes_nacionalidade.prox_nacionalidade = filme
        lista_nacionalidade.quantidade += 1

    def mostra_dados(self):
        lista_geral = self.multilista.primeiro_geral
        while lista_geral:
            self.tela.mostra_filmes(lista_geral.nome, lista_geral.ano,
                                    lista_geral.genero, lista_geral.nacionalidade)
            lista_geral = lista_geral.proximo

    #### ESSE MÉTODO ESTÁ AQUI PARA MANTER OS ELEMENTOS DE TESTE JÁ ADICIONADOS_complementar
    def adiciona_elemento_complementar(self, nome: str, ano: int,
                          genero: str, nacionalidade: str):
        filme = Filme(nome, ano, genero, nacionalidade)
        self.adiciona_lista_geral(filme)
        self.adiciona_lista_ano(filme)
        self.adiciona_lista_genero(filme)
        self.adiciona_lista_nacionalidade(filme)

##### TESTES

teste = ControladorGeral()

teste.adiciona_elemento_complementar('Star Wars', 1983, 'Sci-Fi', 'USA')
teste.adiciona_elemento_complementar('Harry Potter', 2011, 'Fantasia', 'USA')
teste.adiciona_elemento_complementar('Cidade de Deus', 1999, 'Drama', 'Brasil')
teste.adiciona_elemento_complementar('O Menino e a Garça', 2024, 'Aventura', 'Japão')
teste.adiciona_elemento_complementar('Ford vs Ferrari', 2019, 'Drama', 'USA')
teste.adiciona_elemento_complementar('Parasita', 2019, 'Drama', 'Coreia do Sul')

teste.mostra_dados()