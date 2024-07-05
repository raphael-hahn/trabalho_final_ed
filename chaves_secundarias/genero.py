from chaves_primarias.filme import Filme


class Genero:

    def __init__(self, genero: str, primeiro: Filme):
        self.__genero = genero
        self.__primeiro = primeiro
        self.__quantidade = 1
        self.__prox_genero = None

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero: str):
        if isinstance(genero, str):
            self.__genero = genero

    @property
    def primeiro(self):
        return self.__primeiro

    @primeiro.setter
    def primeiro(self, primeiro: Filme):
        self.__primeiro = primeiro

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade += quantidade

    @property
    def prox_genero(self):
        return self.__prox_genero

    @prox_genero.setter
    def prox_genero(self, prox_genero):
        if isinstance(prox_genero, Genero):
            self.__prox_genero = prox_genero
