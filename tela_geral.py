

class TelaGeral:

    def mostra_filmes(self, nome, ano, genero, nacionalidade):
        print(f'Filme: {nome}, Ano de publicação: {ano}, Gênero: {genero}, Nacionalidade: {nacionalidade}')
        return

    def adiciona_filme(self):
        nome = input("Digite o nome do filme que você deseja inserir: ")
        ano = input("Digite o ano de publicação do filme que você deseja inserir: ")
        genero = input("Digite o gênero do filme que você deseja inserir: ")
        nacionalidade = input("Digite a nacionalidade do filme que você deseja inserir: ")
        return nome, ano, genero, nacionalidade
