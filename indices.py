from chaves_secundarias.ano import Ano
from chaves_secundarias.genero import Genero
from chaves_secundarias.nacionalidade import Nacionalidade
from chaves_primarias.filme import Filme


class IndiceGeral:

    def __init__(self):
        self.__primeiro_ano = None
        self.__primeiro_genero = None
        self.__primeiro_nacionalidade = None
        self.__primeiro_geral = None

    @property
    def primeiro_ano(self):
        return self.__primeiro_ano

    @primeiro_ano.setter
    def primeiro_ano(self, primeiro_ano: Ano):
        if isinstance(primeiro_ano, Ano):
            self.__primeiro_ano = primeiro_ano

    @property
    def primeiro_genero(self):
        return self.__primeiro_genero

    @primeiro_genero.setter
    def primeiro_genero(self, primeiro_genero: Genero):
        if isinstance(primeiro_genero, Genero):
            self.__primeiro_genero = primeiro_genero

    @property
    def primeiro_nacionalidade(self):
        return self.__primeiro_nacionalidade

    @primeiro_nacionalidade.setter
    def primeiro_nacionalidade(self, primeiro_nacionalidade: Nacionalidade):
        if isinstance(primeiro_nacionalidade, Nacionalidade):
            self.__primeiro_nacionalidade = primeiro_nacionalidade

    @property
    def primeiro_geral(self):
        return self.__primeiro_geral

    @primeiro_geral.setter
    def primeiro_geral(self, primeiro_geral: Filme):
        if isinstance(primeiro_geral, Filme):
            self.__primeiro_geral = primeiro_geral
