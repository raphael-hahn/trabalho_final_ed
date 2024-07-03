from chaves_primarias.filme import Filme


class Nacionalidade:

    def __init__(self, nacionalidade: str, primeiro: Filme):
        self.__nacionalidade = nacionalidade
        self.__primeiro = primeiro
        self.__quantidade = 1
        self.__prox_nacionalidade = None

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade: str):
        if isinstance(nacionalidade, str):
            self.__nacionalidade = nacionalidade

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
    def prox_nacionalidade(self):
        return self.__prox_nacionalidade

    @prox_nacionalidade.setter
    def prox_nacionalidade(self, prox_nacionalidade):
        if isinstance(prox_nacionalidade, Nacionalidade):
            self.__prox_nacionalidade = prox_nacionalidade
