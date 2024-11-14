
import mysql.connector
from mysql.connector import Error

# Classe que irá rodar a aplicação 
class Aplicacao():
    def __init__(self, cursor, conecao) -> None:
        self.cursor_classe = cursor
        self.conecao = conecao

# Função para adicionar um desenvolvedor
    def adicionar_desenvolvedor(self,nome):
        try:
            self.cursor_classe.execute('INSERT INTO Desenvolvedor (nome) VALUES (%s)', (nome,))
            self.conecao.commit()
            print("Desenvolvedor adicionado com sucesso!")
        except Error as e:
            print(f"Erro ao adicionar desenvolvedor: {e}")

    # Função para adicionar um jogo
    def adicionar_jogo(self,nome, ano_lancamento, plataformas, desenvolvedor_id):
        try:
            self.cursor_classe.execute('''
            INSERT INTO Jogo (nome, ano_lancamento, plataformas, nota, desenvolvedor_id)
            VALUES (%s, %s, %s, NULL, %s)
            ''', (nome, ano_lancamento, plataformas, desenvolvedor_id))
            self.conecao.commit()
            print("Jogo adicionado com sucesso!")
        except Error as e:
            print(f"Erro ao adicionar jogo: {e}")

    # Função para deletar um jogo
    def delete_jogo(self, id):
        try:
            self.cursor_classe.execute('DELETE FROM Jogo WHERE id = %s', (id,))
            self.conecao.commit()
            print("Dados deletados com sucesso.")
        except Error as e:
            print(f"Erro ao deletar jogo: {e}")

    # Função para deletar um desenvolvedor
    def delete_desenvolvedor(self, id):
        try:
            self.cursor_classe.execute('DELETE FROM Jogo WHERE desenvolvedor_id = %s', (id,))
            self.conecao.commit()
            self.cursor_classe.execute('DELETE FROM Desenvolvedor WHERE id = %s', (id,))
            self.conecao.commit()
            print("Desenvolvedor deletado com sucesso.")
        except Error as e:
            print(f"Erro ao deletar desenvolvedor: {e}")

    # Função para listar todos os jogos
    def listar_jogos(self):
        try:
            self.cursor_classe.execute('''
            SELECT Jogo.id, Jogo.nome, Jogo.ano_lancamento, Jogo.plataformas, Jogo.nota, Desenvolvedor.nome
            FROM Jogo
            JOIN Desenvolvedor ON Jogo.desenvolvedor_id = Desenvolvedor.id
            ''')
            jogos = self.cursor_classe.fetchall()
            if jogos:
                for jogo in jogos:
                    print(f"ID: {jogo[0]}, Nome: {jogo[1]}, Ano: {jogo[2]}, Plataformas: {jogo[3]}, Nota: {jogo[4]}, Desenvolvedor: {jogo[5]}")
            else:
                return False
            return True
        except Error as e:
            print(f"Erro ao listar jogos: {e}")

    # Função para listar apenas os jogos avaliados
    def listar_jogos_avaliados(self):
        try:
            self.cursor_classe.execute('''
            SELECT Jogo.id, Jogo.nome, Jogo.ano_lancamento, Jogo.plataformas, Jogo.nota, Desenvolvedor.nome
            FROM Jogo
            JOIN Desenvolvedor ON Jogo.desenvolvedor_id = Desenvolvedor.id
            WHERE Jogo.nota IS NOT NULL
            ''')
            jogos = self.cursor_classe.fetchall()
            if jogos:
                print("\n=== Jogos Avaliados ===")
                for jogo in jogos:
                    print(f"ID: {jogo[0]}, Nome: {jogo[1]}, Ano: {jogo[2]}, Plataformas: {jogo[3]}, Nota: {jogo[4]}, Desenvolvedor: {jogo[5]}")
            else:
                print("Nenhum jogo avaliado.")
        except Error as e:
            print(f"Erro ao listar jogos avaliados: {e}")

    # Função para adicionar uma nota a um jogo
    def adicionar_nota(self,jogo_id, nota):
        try:
            self.cursor_classe.execute('UPDATE Jogo SET nota = %s WHERE id = %s', (nota, jogo_id))
            self.conecao.commit()
            print("Nota adicionada com sucesso!")
        except Error as e:
            print(f"Erro ao adicionar nota ao jogo: {e}")
 
    # Função para listar desenvolvedores
    def listar_desenvolvedores(self):
        try:
            self.cursor_classe.execute("SELECT * FROM Desenvolvedor")
            desenvolvedores = self.cursor_classe.fetchall()
            if desenvolvedores:
                for dev in desenvolvedores:
                    print(f"ID: {dev[0]}, Nome: {dev[1]}")
            else:
                return False
            return True
        except Error as e:
            print(f"Erro ao listar desenvolvedores: {e}")

    # Interface para usuário interagir
    def menu(self):
        try:
            while True:
                print("\n=== Menu ===")
                print("1. Adicionar Desenvolvedor")
                print("2. Adicionar Jogo")
                print("3. Deletar Jogo")
                print("4. Deletar Desenvolvedor")
                print("5. Listar Jogos")
                print("6. Adicionar/atualizar Nota a um Jogo")
                print("7. Listar Jogos Avaliados")
                print("8. Sair")
                opcao = input("Escolha uma opção: ")

                if opcao == '1':
                    try:
                        nome = input("Digite o nome do desenvolvedor: ")
                        self.adicionar_desenvolvedor(nome)
                    except Exception as e:
                        print(f"Erro ao adicionar desenvolvedores: {e}")
                    

                elif opcao == '2':
                    try:
                        self.cursor_classe.execute("SELECT * FROM Desenvolvedor")
                        desenvolvedores = self.cursor_classe.fetchall()
                        if desenvolvedores:
                            nome = input("Digite o nome do jogo: ")
                            ano = int(input("Digite o ano de lançamento: "))
                            plataformas = input("Digite a plataforma que você jogou: ")
                            self.listar_desenvolvedores()
                            desenvolvedor_id = int(input("Digite o ID do desenvolvedor: "))
                            self.adicionar_jogo(nome, ano, plataformas, desenvolvedor_id)
                        else:
                            print('É preciso adicionar pelo menos um desenvolvedor antes de cadastrar um jogo!')

                    except Exception as e:
                        print(f"Erro ao adicionar jogo: {e}")
                
                elif opcao == '3':
                    try:
                        status = self.listar_jogos()
                        if status:
                            jogo_id = int(input("Digite o ID do jogo que deseja excluir da lista: "))
                            self.delete_jogo(jogo_id)
                        else:
                            print('Nenhum jogo cadastrado para excluir!')
                    except Exception as e:
                        print(f"Erro ao deletar jogo: {e}")
                
                elif opcao == '4':
                    try:
                        status = self.listar_desenvolvedores()
                        if status:
                            print("Isso pode excluir jogos associados ao desenvolvedor, cuidado!")
                            desenvoldedor_id = int(input("Digite o ID do Desenvolvedor que deseja excluir da lista: "))
                            self.delete_desenvolvedor(desenvoldedor_id)
                        else:
                            print('Nenhum desenvolvedor cadastrado!')
                    except Exception as e:
                        print(f"Erro ao deletar desenvolvedor: {e}")

                elif opcao == '5':
                    try:
                        status = self.listar_jogos()
                        if not status:
                            print('Nenhum jogo para listar!')
                    except Exception as e:
                        print(f"Erro ao listar jogos: {e}")

                elif opcao == '6':
                    try:
                        status = self.listar_jogos()
                        if status:
                            jogo_id = int(input("Digite o ID do jogo para adicionar/atualizar a nota: "))
                            nota = float(input("Digite a nota (0-10): "))
                            self.adicionar_nota(jogo_id, nota)
                        else:
                            print('Nenhum jogo foi cadastrado para dar/atualizar a nota!')
                    except Exception as e:
                        print(f"Erro ao adicionar nota ao jogo: {e}")

                elif opcao == '7':
                    try:
                        self.listar_jogos_avaliados()
                    except Exception as e:
                        print(f"Erro ao listar jogos avaliados: {e}")

                elif opcao == '8':
                    print("Saindo...")
                    break

                else:
                    print("Opção inválida! Tente novamente.")

        except Error as e:
            print(f"Erro ao excutador o menu: {e}")

# Conectando ao banco de dados MySQL
conn = mysql.connector.connect(
    host='127.0.0.1',     # endereço servidor MySQL
    user='root',   # usuário do banco de dados
    password='', # senha do banco de dados
    database='meusjogos'  # nome do banco de dados
)
#criando o cursor
cursor = conn.cursor()
# Instanciando a classe
app = Aplicacao(cursor, conn)

# Executa o menu
app.menu()
# Fechando a conexão ao banco de dados
cursor.close()
conn.close()