

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

    def menu_opcoes(self):
        print(10*'-=', 'Menu de opções', 10*'-=')
        print('1 - Buscar filme com uma chave secundária')
        print('2 - Buscar filme com duas chaves secundárias')
        print('3 - Incluir novo filme')
        print('4 - Excluir filme')
        print('5 - Busca geral')
        print('6 - Interromper a aplicação')
        while True:
            try:
                opcao = int(input("Digite a opção de sua escolha: "))
                if opcao not in range(1,7):
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor inválido! Por favor, insira um número que represente uma das opções.")

    def escolhe_chave(self):
        print(10*'-=', 'Menu de opções', 10*'-=')
        print('1 - Buscar filmes a partir do ano de lançamento')
        print('2 - Buscar filmes a partir do seu gênero')
        print('3 - Buscar filmes a partir da sua nacionalidade')
        while True:
            try:
                opcao = int(input("Digite a opção de sua escolha: "))
                if opcao not in range(1,4):
                    raise ValueError
                return opcao
            except ValueError:
                print("Valor inválido! Por favor, insira um número que represente uma das opções.")

    def escolhe_chave_dupla(self):
        print(10*'-=', 'Menu de opções', 10*'-=')
        print('1 - Buscar filmes a partir do ano de lançamento')
        print('2 - Buscar filmes a partir do seu gênero')
        print('3 - Buscar filmes a partir da sua nacionalidade')
        while True:
            try:
                opcao1 = int(input("Digite a primeira chave de sua escolha: "))
                if opcao1 not in range(1,4):
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido! Por favor, insira um número que represente uma das opções.")
        while True:
            try:
                opcao2 = int(input("Digite a segunda chave de sua escolha: "))
                if opcao2 not in range(1,4) or opcao2 == opcao1:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido! Por favor, insira um número que represente uma das opções e que não tenha sido escolhido anteriormente.")
        return opcao1, opcao2
