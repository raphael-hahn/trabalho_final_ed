

class TelaGeral:

    def mostra_filmes(self, nome, ano, genero, nacionalidade):
        print(f'Filme: {nome}, Ano de publicação: {ano}, Gênero: {genero}, Nacionalidade: {nacionalidade}')
        return

    def lista_vazia(self):
        print("A lista está vazia!")

    def valor_nao_existente(self):
        print('Os valores referentes à chave fornecida não foram encontrados ou não existem!')

    def adiciona_filme(self):
        nome = input("Digite o nome do filme que você deseja inserir: ")
        ano = input("Digite o ano de publicação do filme que você deseja inserir: ")
        genero = input("Digite o gênero do filme que você deseja inserir: ")
        nacionalidade = input("Digite a nacionalidade do filme que você deseja inserir: ")
        return nome, ano, genero, nacionalidade

    def insere_ano(self):
        while True:
            try:
                ano = int(input("Digite o ano de publicação do filme: "))
                return ano
            except ValueError:
                print("Valor inválido! Por favor, insira um número inteiro.")

    def insere_genero(self):
        while True:
            try:
                genero = input("Digite o gênero do filme: ")
                return genero
            except ValueError:
                print("Valor inválido! Por favor, insira o nome do gênero como ele foi adicionado.")

    def insere_nacionalidade(self):
        while True:
            try:
                nacionalidade = input("Digite a nacionalidade do filme: ")
                return nacionalidade
            except ValueError:
                print("Valor inválido! Por favor, insira o nome da nacionalidade como ela foi adicionada.")

    def remove_elemento(self):
        nome = input("Digite o nome do filme que deseja excluir: ")
        return nome
