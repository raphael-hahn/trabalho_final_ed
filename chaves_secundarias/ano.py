from chaves_primarias.filme import Filme


class Ano:

    def __init__(self, ano: int, primeiro: Filme):
        self.__ano = ano
        self.__primeiro = primeiro
        self.__quantidade = 1
        self.__prox_ano = None

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        if isinstance(ano, int):
            self.__ano = ano

    @property
    def primeiro(self):
        return self.__primeiro

    @primeiro.setter
    def primeiro(self, primeiro: Filme):
        if isinstance(primeiro, Filme):
            self.__primeiro = primeiro

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade += quantidade

    @property
    def prox_ano(self):
        return self.__prox_ano

    @prox_ano.setter
    def prox_ano(self, prox_ano):
        if isinstance(prox_ano, Ano):
            self.__prox_ano = prox_ano
