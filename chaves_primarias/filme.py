

class Filme:

    def __init__(self, nome: str, ano: int, genero: str, nacionalidade: str ):

        self.__nome = nome
        self.__ano = ano
        self.__prox_ano = None
        self.__genero = genero
        self.__prox_genero = None
        self.__nacionalidade = nacionalidade
        self.__prox_nacionalidade = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, str):
            self.__ano = ano

    @property
    def prox_ano(self):
        return self.__prox_ano

    @prox_ano.setter
    def prox_ano(self, prox_ano):
        if isinstance(prox_ano, Filme):
            self.__prox_ano = prox_ano

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if isinstance(genero, str):
            self.__genero = genero

    @property
    def prox_genero(self):
        return self.__prox_genero

    @prox_genero.setter
    def prox_genero(self, prox_genero):
        if isinstance(prox_genero, Filme):
            self.__prox_genero = prox_genero

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        if isinstance(nacionalidade, str):
            self.__nacionalidade = nacionalidade

    @property
    def prox_nacionalidade(self):
        return self.__prox_nacionalidade

    @prox_nacionalidade.setter
    def prox_nacionalidade(self, prox_nacionalidade):
        if isinstance(prox_nacionalidade, Filme):
            self.__prox_nacionalidade = prox_nacionalidade
