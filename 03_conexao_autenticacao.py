import sqlite3
from pathlib import Path

# Definindo o caminho do banco de dados
ROOT_PATH = Path(__file__).parent
# Conectando ao banco de dados SQLite
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
# Criando um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Função para criar a tabela "clientes"
def criar_tabela(conexao, cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome VARCHAR(100), 
        email VARCHAR(150), 
        senha VARCHAR(150)
    )
    ''')
    # Confirmando as mudanças
    conexao.commit()

# Função para inserir um registro na tabela "clientes"
def inserir_registro(conexao, cursor, nome, email, senha):
    # Dados a serem inseridos
    data = (nome, email, senha)
    # Inserindo os dados na tabela "clientes"
    cursor.execute("INSERT INTO clientes (nome, email, senha) VALUES (?, ?, ?)", data)
    # Confirmando as mudanças
    conexao.commit()

# Função para atualizar um registro na tabela "clientes"
def atualizar_registro(conexao, cursor, nome, email, senha, id):
    data = (nome, email, senha, id)
    cursor.execute("UPDATE clientes SET nome=?, email=?, senha=? WHERE id=?", data)
    # Confirmando as mudanças
    conexao.commit()

# Função para excluir um registro da tabela "clientes"
def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()

# Função para autenticar um usuário
def autenticar_usuario(cursor, email, senha):
    data = (email, senha)
    cursor.execute("SELECT * FROM clientes WHERE email=? AND senha=?", data)
    usuario = cursor.fetchone()
    if usuario:
        print("Autenticação bem-sucedida")
        return True
    else:
        print("Falha na autenticação")
        return False

# Criar a tabela (caso ainda não exista)
criar_tabela(conexao, cursor)

# Inserir alguns registros para teste
# inserir_registro(conexao, cursor, 'Rafael', 'rafaeltecsuporte@gmail.com', '12345678')
# inserir_registro(conexao, cursor, 'Ana', 'ana@example.com', 'senha123')

# Testar a autenticação
# autenticar_usuario(cursor, 'rafaeltecsuporte@gmail.com', '12345678')
# autenticar_usuario(cursor, 'ana@example.com', 'senha123')
# autenticar_usuario(cursor, 'joao@example.com', 'pass123')

#terminal informar o user e senha
#email = input("Informe seu email: ")
#senha = input("Informe sua senha: ")
# Testar a autenticação
#autenticar_usuario(cursor, email, senha)


def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email, senha) VALUES (?,?,?)", dados)
    conexao.commit()

# inserir_muitos(conexao, cursor, dados)  

# dados = [
#     ('Guilherme', 'gui123@hotmail.com', '123mudar'),
    
# 
# Fechando a conexão com o banco de dados
#conexao.close()

# Função para recuperar um cliente pelo ID
def recuperar_cliente(cursor, id):
    """Recupera um cliente pelo ID."""
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = recuperar_cliente(cursor,1)
print(cliente)


