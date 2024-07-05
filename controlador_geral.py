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
        return

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
        lista_ano.quantidade = 1

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
        lista_genero.quantidade = 1

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
        lista_nacionalidade.quantidade = 1

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
                lista_chave.quantidade = -1
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
                lista_chave.quantidade = -1
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
                lista_chave.quantidade = -1
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

    #### FAZ BUSCA COMPOSTA DE ANO COM GÊNERO
    def busca_ano_genero(self):
        ano = self.tela.insere_ano()
        lista_chave_ano = self.multilista.primeiro_ano
        while lista_chave_ano:
            if lista_chave_ano.ano == ano:
                lista_ano = lista_chave_ano.primeiro
                quantidade_ano = lista_chave_ano.quantidade
                break
            lista_chave_ano = lista_chave_ano.prox_ano
            if lista_chave_ano is None: #### PARA E EXECUÇÃO CASO A CHAVE SECUNDÁRIA PASSADA NÃO EXISTA
                self.tela.valor_nao_existente()
                return

        genero = self.tela.insere_genero()
        lista_chave_genero = self.multilista.primeiro_genero
        while lista_chave_genero:
            if lista_chave_genero.genero == genero:
                lista_genero = lista_chave_genero.primeiro
                quantidade_genero = lista_chave_genero.quantidade
                break
            lista_chave_genero = lista_chave_genero.prox_genero
            if lista_chave_genero is None:
                self.tela.valor_nao_existente()
                return

        if quantidade_ano <= quantidade_genero:
            while lista_ano:
                if lista_ano.genero == genero:
                    self.tela.mostra_filmes(lista_ano.nome, lista_ano.ano,
                                            lista_ano.genero, lista_ano.nacionalidade)
                lista_ano = lista_ano.prox_ano
            return

        if quantidade_genero <= quantidade_ano:
            while lista_genero:
                if lista_genero.ano == ano:
                    self.tela.mostra_filmes(lista_genero.nome, lista_genero.ano,
                                            lista_genero.genero, lista_genero.nacionalidade)
                lista_genero = lista_genero.prox_genero
            return

    #### FAZ BUSCA COMPOSTA DE ANO COM NACIONALIDADE
    def busca_ano_nacionalidade(self):
        ano = self.tela.insere_ano()
        lista_chave_ano = self.multilista.primeiro_ano
        while lista_chave_ano:
            if lista_chave_ano.ano == ano:
                lista_ano = lista_chave_ano.primeiro
                quantidade_ano = lista_chave_ano.quantidade
                break
            lista_chave_ano = lista_chave_ano.prox_ano
            if lista_chave_ano is None:
                self.tela.valor_nao_existente()
                return

        nacionalidade = self.tela.insere_nacionalidade()
        lista_chave_nacionalidade = self.multilista.primeiro_nacionalidade
        while lista_chave_nacionalidade:
            if lista_chave_nacionalidade.nacionalidade == nacionalidade:
                lista_nacionalidade = lista_chave_nacionalidade.primeiro
                quantidade_nacionalidade = lista_chave_nacionalidade.quantidade
                break
            lista_chave_nacionalidade = lista_chave_nacionalidade.prox_nacionalidade
            if lista_chave_nacionalidade is None:
                self.tela.valor_nao_existente()
                return

        if quantidade_ano <= quantidade_nacionalidade:
            while lista_ano: #### AQUI PODE DAR PROBLEMA SE TIVER SÓ UM ELEMENTO
                if lista_ano.nacionalidade == nacionalidade:
                    self.tela.mostra_filmes(lista_ano.nome, lista_ano.ano,
                                            lista_ano.genero, lista_ano.nacionalidade)
                lista_ano = lista_ano.prox_ano
            return

        if quantidade_nacionalidade <= quantidade_ano:
            while lista_nacionalidade: #### AQUI PODE DAR PROBLEMA SE TIVER SÓ UM ELEMENTO
                if lista_nacionalidade.ano == ano:
                    self.tela.mostra_filmes(lista_nacionalidade.nome, lista_nacionalidade.ano,
                                            lista_nacionalidade.genero, lista_nacionalidade.nacionalidade)
                lista_nacionalidade = lista_nacionalidade.prox_nacionalidade
            return

    #### FAZ BUSCA COMPOSTA DE GÊNERO COM NACIONALIDADE
    def busca_genero_nacionalidade(self):
        genero = self.tela.insere_genero()
        lista_chave_genero = self.multilista.primeiro_genero
        while lista_chave_genero:
            if lista_chave_genero.genero == genero:
                lista_genero = lista_chave_genero.primeiro
                quantidade_genero = lista_chave_genero.quantidade
                break
            lista_chave_genero = lista_chave_genero.prox_genero
            if lista_chave_genero is None:
                self.tela.valor_nao_existente()
                return

        nacionalidade = self.tela.insere_nacionalidade()
        lista_chave_nacionalidade = self.multilista.primeiro_nacionalidade
        while lista_chave_nacionalidade:
            if lista_chave_nacionalidade.nacionalidade == nacionalidade:
                lista_nacionalidade = lista_chave_nacionalidade.primeiro
                quantidade_nacionalidade = lista_chave_nacionalidade.quantidade
                break
            lista_chave_nacionalidade = lista_chave_nacionalidade.prox_nacionalidade
            if lista_chave_nacionalidade is None:
                self.tela.valor_nao_existente()
                return

        if quantidade_genero <= quantidade_nacionalidade:
            while lista_genero: #### AQUI PODE DAR PROBLEMA SE TIVER SÓ UM ELEMENTO
                if lista_genero.nacionalidade == nacionalidade:
                    self.tela.mostra_filmes(lista_genero.nome, lista_genero.ano,
                                            lista_genero.genero, lista_genero.nacionalidade)
                lista_genero = lista_genero.prox_genero
            return

        if quantidade_nacionalidade <= quantidade_genero:
            while lista_nacionalidade: #### AQUI PODE DAR PROBLEMA SE TIVER SÓ UM ELEMENTO
                if lista_nacionalidade.genero == genero:
                    self.tela.mostra_filmes(lista_nacionalidade.nome, lista_nacionalidade.ano,
                                            lista_nacionalidade.genero, lista_nacionalidade.nacionalidade)
                lista_nacionalidade = lista_nacionalidade.prox_nacionalidade
            return

    def menu_opcoes(self):
        while True:
            opcao = self.tela.menu_opcoes()
            if opcao == 1:
                self.menu_busca_chave_unica()
            if opcao == 2:
                self.menu_busca_chave_dupla()
            if opcao == 3:
                self.adiciona_elemento()
            if opcao == 4:
                self.remove_elemento_menu()
            if opcao == 5:
                self.mostra_dados_geral()
            if opcao == 6:
                return

    def menu_busca_chave_unica(self):
        chave = self.tela.escolhe_chave()
        if chave == 1:
            self.mostra_dados_ano()
        if chave == 2:
            self.mostra_dados_genero()
        if chave == 3:
            self.mostra_dados_nacionalidade()
        return

    def menu_busca_chave_dupla(self):
        chave1, chave2 = self.tela.escolhe_chave_dupla()
        if (chave1 == 1 and chave2 == 2) or (chave2 == 1 and chave1 == 2):
            self.busca_ano_genero()
        if (chave1 == 1 and chave2 == 2) or (chave2 == 1 and chave1 == 2):
            self.busca_ano_genero()
        if (chave1 == 1 and chave2 == 3) or (chave2 == 1 and chave1 == 3):
            self.busca_ano_nacionalidade()
        if (chave1 == 2 and chave2 == 3) or (chave2 == 2 and chave1 == 3):
            self.busca_genero_nacionalidade()
        return

    #### CRIA VÁRIAS INSTÂNCIAS PRÉVIAS PARA FACILITAR A CORREÇÃO DO CÓDIGO
    def inicializa_elementos(self):
        self.adiciona_elemento_complementar('Star Wars', 1977, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('Harry Potter', 2011, 'Fantasia', 'USA')
        self.adiciona_elemento_complementar('Cidade de Deus', 2002, 'Drama', 'Brasil')
        self.adiciona_elemento_complementar('O Menino e a Garça', 2024, 'Aventura', 'Japão')
        self.adiciona_elemento_complementar('Ford vs Ferrari', 2019, 'Drama', 'USA')
        self.adiciona_elemento_complementar('Parasita', 2019, 'Drama', 'Coreia do Sul')
        self.adiciona_elemento_complementar('Inception', 2010, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('O Senhor dos Anéis', 2003, 'Fantasia', 'Nova Zelândia')
        self.adiciona_elemento_complementar('Pantera Negra', 2018, 'Ação', 'USA')
        self.adiciona_elemento_complementar('Coringa', 2019, 'Drama', 'USA')
        self.adiciona_elemento_complementar('Vingadores: Ultimato', 2019, 'Ação', 'USA')
        self.adiciona_elemento_complementar('A Viagem de Chihiro', 2001, 'Fantasia', 'Japão')
        self.adiciona_elemento_complementar('A Vida é Bela', 1997, 'Drama', 'Itália')
        self.adiciona_elemento_complementar('O Labirinto do Fauno', 2006, 'Fantasia', 'México')
        self.adiciona_elemento_complementar('Interstellar', 2014, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('A Origem dos Guardiões', 2012, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Cisne Negro', 2010, 'Drama', 'USA')
        self.adiciona_elemento_complementar('A Rede Social', 2010, 'Drama', 'USA')
        self.adiciona_elemento_complementar('Bacurau', 2019, 'Drama', 'Brasil')
        self.adiciona_elemento_complementar('Tropa de Elite', 2007, 'Ação', 'Brasil')
        self.adiciona_elemento_complementar('Matrix', 1999, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('Gladiador', 2000, 'Ação', 'USA')
        self.adiciona_elemento_complementar('Pulp Fiction', 1994, 'Crime', 'USA')
        self.adiciona_elemento_complementar('O Poderoso Chefão', 1972, 'Crime', 'USA')
        self.adiciona_elemento_complementar('O Cavaleiro das Trevas', 2008, 'Ação', 'USA')
        self.adiciona_elemento_complementar('Forrest Gump', 1994, 'Drama', 'USA')
        self.adiciona_elemento_complementar('Clube da Luta', 1999, 'Drama', 'USA')
        self.adiciona_elemento_complementar('O Rei Leão', 1994, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Titanic', 1997, 'Romance', 'USA')
        self.adiciona_elemento_complementar('Avatar', 2009, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('Jurassic Park', 1993, 'Aventura', 'USA')
        self.adiciona_elemento_complementar('Star Wars: O Despertar da Força', 2015, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('Os Incríveis', 2004, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Toy Story', 1995, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Coco', 2017, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Viva - A Vida é uma Festa', 2017, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Homem-Aranha: No Aranhaverso', 2018, 'Animação', 'USA')
        self.adiciona_elemento_complementar('O Silêncio dos Inocentes', 1991, 'Thriller', 'USA')
        self.adiciona_elemento_complementar('Django Livre', 2012, 'Western', 'USA')
        self.adiciona_elemento_complementar('O Grande Hotel Budapeste', 2014, 'Comédia', 'USA')
        self.adiciona_elemento_complementar('A Bela e a Fera', 1991, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Moana', 2016, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Valente', 2012, 'Animação', 'USA')
        self.adiciona_elemento_complementar('Divertida Mente', 2015, 'Animação', 'USA')
        self.adiciona_elemento_complementar('WALL-E', 2008, 'Animação', 'USA')
        self.adiciona_elemento_complementar('O Fabuloso Destino de Amélie Poulain', 2001, 'Romance', 'França')
        self.adiciona_elemento_complementar('Whiplash', 2014, 'Drama', 'USA')
        self.adiciona_elemento_complementar('La La Land', 2016, 'Musical', 'USA')
        self.adiciona_elemento_complementar('Cidadão Kane', 1941, 'Drama', 'USA')
        self.adiciona_elemento_complementar('Casablanca', 1942, 'Romance', 'USA')
        self.adiciona_elemento_complementar('12 Anos de Escravidão', 2013, 'Drama', 'USA')
        self.adiciona_elemento_complementar('Guerra nas Estrelas', 1977, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('O Exorcista', 1973, 'Horror', 'USA')
        self.adiciona_elemento_complementar('E.T. - O Extraterrestre', 1982, 'Sci-Fi', 'USA')
        self.adiciona_elemento_complementar('Duro de Matar', 1988, 'Ação', 'USA')
        self.adiciona_elemento_complementar('Indiana Jones e os Caçadores da Arca Perdida', 1981, 'Aventura', 'USA')
        self.adiciona_elemento_complementar('De Volta para o Futuro', 1985, 'Sci-Fi', 'USA')
        self.menu_opcoes()
        return
