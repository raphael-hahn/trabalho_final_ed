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

    #### MOSTRA TODOS OS ELEMENTOS DA LISTA
    def mostra_dados_geral(self):
        lista_geral = self.multilista.primeiro_geral
        while lista_geral:
            self.tela.mostra_filmes(lista_geral.nome, lista_geral.ano,
                                    lista_geral.genero, lista_geral.nacionalidade)
            lista_geral = lista_geral.proximo
        return

    #### FAZ A LÓGICA PARA ENCONTRAR OS VALORES REFERENTES A UMA CHAVE SECUNDÁRIA DE ANO
    def mostra_dados_ano(self):
        ano = self.tela.insere_ano()
        lista_ano = self.multilista.primeiro_ano
        if lista_ano == None:
            self.tela.lista_vazia()
            return
        while lista_ano:
            if lista_ano.ano == ano:
                self.exibe_dados_ano(lista_ano.primeiro)
                return
            lista_ano = lista_ano.prox_ano
        self.tela.valor_nao_existente()
        return

    #### ESSE MÉTODO ENVIA OS VALORES PARA A TELA REFERENTES À CHAVE SECUNDÁRIA DE ANO FORNECIDA PELO USUÁRIO
    def exibe_dados_ano(self, lista_dados: Filme):
        while lista_dados:
            self.tela.mostra_filmes(lista_dados.nome, lista_dados.ano,
                                    lista_dados.genero, lista_dados.nacionalidade)
            lista_dados = lista_dados.prox_ano

    #### FAZ A LÓGICA PARA ENCONTRAR OS VALORES REFERENTES A UMA CHAVE SECUNDÁRIA DE GÊNERO
    def mostra_dados_genero(self):
        genero = self.tela.insere_genero()
        lista_genero = self.multilista.primeiro_genero
        if lista_genero == None:
            self.tela.lista_vazia()
            return
        while lista_genero:
            if lista_genero.genero == genero:
                self.exibe_dados_genero(lista_genero.primeiro)
                return
            lista_genero = lista_genero.prox_genero
        self.tela.valor_nao_existente()
        return

    #### ESSE MÉTODO ENVIA OS VALORES PARA A TELA REFERENTES À CHAVE SECUNDÁRIA DE GÊNERO FORNECIDA PELO USUÁRIO
    def exibe_dados_genero(self, lista_dados: Filme):
        while lista_dados:
            self.tela.mostra_filmes(lista_dados.nome, lista_dados.ano,
                                    lista_dados.genero, lista_dados.nacionalidade)
            lista_dados = lista_dados.prox_genero

    #### FAZ A LÓGICA PARA ENCONTRAR OS VALORES REFERENTES A UMA CHAVE SECUNDÁRIA DE NACIONALIDADE
    def mostra_dados_nacionalidade(self):
        nacionalidade = self.tela.insere_nacionalidade()
        lista_nacionalidade = self.multilista.primeiro_nacionalidade
        if lista_nacionalidade == None:
            self.tela.lista_vazia()
            return
        while lista_nacionalidade:
            if lista_nacionalidade.nacionalidade == nacionalidade:
                self.exibe_dados_nacionalidade(lista_nacionalidade.primeiro)
                return
            lista_nacionalidade = lista_nacionalidade.prox_nacionalidade
        self.tela.valor_nao_existente()
        return

    #### ESSE MÉTODO ENVIA OS VALORES PARA A TELA REFERENTES À CHAVE SECUNDÁRIA DE GÊNERO FORNECIDA PELO USUÁRIO
    def exibe_dados_nacionalidade(self, lista_dados: Filme):
        while lista_dados:
            self.tela.mostra_filmes(lista_dados.nome, lista_dados.ano,
                                    lista_dados.genero, lista_dados.nacionalidade)
            lista_dados = lista_dados.prox_nacionalidade

    #### ESSE MÉTODO ESTÁ AQUI PARA MANTER OS ELEMENTOS DE TESTE JÁ ADICIONADOS_complementar
    def adiciona_elemento_complementar(self, nome: str, ano: int,
                          genero: str, nacionalidade: str):
        filme = Filme(nome, ano, genero, nacionalidade)
        self.adiciona_lista_geral(filme)
        self.adiciona_lista_ano(filme)
        self.adiciona_lista_genero(filme)
        self.adiciona_lista_nacionalidade(filme)

    def remove_elemento_menu(self):
        if self.multilista.primeiro_geral == None: #### VERIFICA SE A LISTA ESTÁ VAZIA, NÃO VAI MAIS SER VERIFICADO, ENTÃO O CÓDIGO PRECISA ESTAR FUNCIONANDO BEM PARA NÃO DAR PROBLEMA
            self.tela.lista_vazia()
            return
        nome = self.tela.remove_elemento() #### BUSCA COM O USUÁRIO O ELEMENTO A SER REMOVIDO
        ano, genero, nacionalidade = self.remove_elemento_geral(nome)
        if ano == 0:
            return
        self.remove_elemento_ano(nome, ano)
        self.remove_elemento_genero(nome, genero)
        self.remove_elemento_nacionalidade(nome, nacionalidade)
        return

    def remove_elemento_geral(self, nome: str):
        lista_geral = self.multilista.primeiro_geral
        if nome == lista_geral.nome:
            if lista_geral.proximo != None: #### VERIFICA SE TÊM MAIS DE UM ELEMENTO NA LISTA
                self.multilista.primeiro_geral = lista_geral.proximo #### ATRIBUI A PRIMEIRA POSIÇÃO AO VALOR SEGUINTE DO REMOVIDO
            else:
                self.multilista.primeiro_geral = None #### A LISTA SÓ TINHA UM ELEMENTO E AGORA ESTÁ VAZIA
            return lista_geral.ano, lista_geral.genero, lista_geral.nacionalidade
        while lista_geral.proximo:
            if nome == lista_geral.proximo.nome: #### VERIFICA SEMPRE SE O PRÓXIMO É O ELEMENTO QUE PROCURAMOS
                ano = lista_geral.proximo.ano
                genero = lista_geral.proximo.genero
                nacionalidade = lista_geral.proximo.nacionalidade
                if lista_geral.proximo.proximo is None: #### VERIFICA SE EXISTE PRÓXIMO DO PRÓXIMO
                    lista_geral.proximo = None #### NÃO EXISTINDO, O PRÓXIMO SE TORNA "None" AO FAZER A REMOÇÃO DO ELEMENTO
                else:
                    lista_geral.proximo = lista_geral.proximo.proximo #### O PRÓXIMO VIRA O PRÓXIMO DO PRÓXIMO
                return ano, genero, nacionalidade
            lista_geral = lista_geral.proximo
        self.tela.valor_nao_existente()
        return 0, 0, 0 #### RETORNA "0s" PARA PARAR A EXECUÇÃO DA REMOÇÃO

    def remove_elemento_ano(self, nome: str, ano: int):
        lista_chave = self.multilista.primeiro_ano
        while lista_chave:
            if lista_chave.ano == ano:
                lista_ano = lista_chave.primeiro
                if nome == lista_ano.nome:
                    if lista_ano.prox_ano != None:
                        lista_chave.primeiro = lista_ano.prox_ano
                    else:
                        lista_chave.primeiro = None
                    return
                while lista_ano.prox_ano:
                    if nome == lista_ano.prox_ano.nome:
                        if lista_ano.prox_ano.prox_ano == None:
                            lista_ano.prox_ano = None
                        else:
                            lista_ano.prox_ano = lista_ano.prox_ano.prox_ano
                        return
                    lista_ano = lista_ano.prox_ano
            lista_chave = lista_chave.prox_ano

    def remove_elemento_genero(self, nome: str, genero: str):
        lista_chave = self.multilista.primeiro_genero
        while lista_chave:
            if lista_chave.genero == genero:
                lista_genero = lista_chave.primeiro
                if nome == lista_genero.nome:
                    if lista_genero.prox_genero != None:
                        lista_chave.primeiro = lista_genero.prox_genero
                    else:
                        lista_chave.primeiro = None
                    return
                while lista_genero.prox_genero:
                    if nome == lista_genero.prox_genero.nome:
                        if lista_genero.prox_genero.prox_genero == None:
                            lista_genero.prox_genero = None
                        else:
                            lista_genero.prox_genero = lista_genero.prox_genero.prox_genero
                        return
                    lista_genero = lista_genero.prox_genero
            lista_chave = lista_chave.prox_genero

    def remove_elemento_nacionalidade(self, nome: str, nacionalidade: str):
        lista_chave = self.multilista.primeiro_nacionalidade
        while lista_chave:
            if lista_chave.nacionalidade == nacionalidade:
                lista_nacionalidade = lista_chave.primeiro
                if nome == lista_nacionalidade.nome:
                    if lista_nacionalidade.prox_nacionalidade != None:
                        lista_chave.primeiro = lista_nacionalidade.prox_nacionalidade
                    else:
                        lista_chave.primeiro = None
                    return
                while lista_nacionalidade.prox_nacionalidade:
                    if nome == lista_nacionalidade.prox_nacionalidade.nome:
                        if lista_nacionalidade.prox_nacionalidade.prox_nacionalidade == None:
                            lista_nacionalidade.prox_nacionalidade = None
                        else:
                            lista_nacionalidade.prox_nacionalidade = lista_nacionalidade.prox_nacionalidade.prox_nacionalidade
                        return
                    lista_nacionalidade = lista_nacionalidade.prox_nacionalidade
            lista_chave = lista_chave.prox_nacionalidade

##### TESTES

teste = ControladorGeral()

teste.adiciona_elemento_complementar('Star Wars', 1983, 'Sci-Fi', 'USA')
teste.adiciona_elemento_complementar('Harry Potter', 2011, 'Fantasia', 'USA')
teste.adiciona_elemento_complementar('Cidade de Deus', 1999, 'Drama', 'Brasil')
teste.adiciona_elemento_complementar('O Menino e a Garça', 2024, 'Aventura', 'Japão')
teste.adiciona_elemento_complementar('Ford vs Ferrari', 2019, 'Drama', 'USA')
teste.adiciona_elemento_complementar('Parasita', 2019, 'Drama', 'Coreia do Sul')

#teste.mostra_dados_ano()
#teste.mostra_dados_genero()

teste.remove_elemento_menu()
teste.mostra_dados_geral()
teste.mostra_dados_ano()
teste.mostra_dados_genero()
teste.mostra_dados_nacionalidade()
