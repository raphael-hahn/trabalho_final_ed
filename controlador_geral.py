from indices import IndiceGeral
from chaves_primarias.filme import Filme
from chaves_secundarias.ano import Ano


class ControladorGeral:

    def __init__(self):
        self.__multilista = IndiceGeral()

    @property
    def multilista(self):
        return self.__multilista

    #### ESSE MÉTODO VAI CHAMAR OS MÉTODOS DE ADIÇÃO DOS 4 TIPOS DE LISTAS PARA ENCADEAR O NOVO ELEMENTO EM CADA UMA DAS CATEGORIAS
    def adiciona_elemento(self, nome: str, ano: int,
                          genero: str, nacionalidade: str): #### TALVEZ RODAR O MÉTODO SÓ COM "self" E PEDIR OS DADOS PARA UM VIEW
        pass

    def adiciona_lista_geral(self, filme: Filme):
        lista_geral = self.multilista.primeiro_geral
        if lista_geral == None:
            lista_geral = filme
            return
        while lista_geral.proximo:
            lista_geral = lista_geral.proximo
        lista_geral.proximo = filme
        return

    def adiciona_lista_ano(self, filme: Filme):
        lista_ano = self.multilista.primeiro_ano
        if lista_ano == None:
            lista_ano.primeiro_ano = Ano(filme.ano, filme)
            return
        while True:
            if filme.ano == lista_ano:
                self.adiciona_ano(filme, lista_ano) #### QUANDO ENCONTRA QUAL CATEGORIA A CHAVE SECUNDÁRIA PERTENCE, CHAMA O MÉTODO PARA SER ENCADEADA NO FINAL DA LISTA
                return
            if lista_ano.prox_ano == None:
                lista_ano.prox_ano = Ano(filme.ano, filme)
                return
            lista_ano = lista_ano.prox_ano

    def adiciona_ano(self, filme: Filme, lista_ano: Ano): #### PODE ACABAR SE TRANSFORMANDO EM UM MÉTODO GERAL DAS CHAVES SECUNDÁRIAS
        lista_filmes_ano = lista_ano.primeiro #### AQUI OS ELEMENTOS ESTÃO A NÍVEL DA CLASSE FILME
        while lista_filmes_ano.prox_ano: #### ENTRA EM UM LOOP QUE É INTERROMPIDO QUANDO O PRÓXIMO VALOR FOR NULO, SIGNIFICANDO QUE ESTÁ NO FINAL DA LISTA
            lista_filmes_ano = lista_filmes_ano.prox_ano #### AVANÇA UMA POSIÇÃO DA LISTA
        lista_filmes_ano.prox_ano = filme #### INSERE O VALOR NA ÚLTIMA POSIÇÃO DO ENCADEAMENTO DA CHAVE SECUNDÁRIA
        lista_ano.quantidade = 1 #### ADICIONA "1" NA CONTAGEM DE ELEMENTOS DA LISTA
        return
