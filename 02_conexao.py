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


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?", data)
    conexao.commit()

#excluir_registro(conexao, cursor, 5)

# Inserir um registro
# inserir_registro(conexao, cursor, 'Rafael', 'rafaeltecsuporte@gmail.com', '12345678')

# inserir_registro(conexao, cursor, 'Rafael', 'rafaeltecsuporte@gmail.com', '12345678')
# inserir_registro(conexao, cursor, 'Ana', 'ana@example.com', 'senha123')
# inserir_registro(conexao, cursor, 'João', 'joao@example.com', 'pass123')
# inserir_registro(conexao, cursor, 'Maria', 'maria@example.com', '123senha')
# inserir_registro(conexao, cursor, 'Pedro', 'pedro@example.com', '1234')
# inserir_registro(conexao, cursor, 'Mariana', 'mariana@example.com', 'pass5678')
# inserir_registro(conexao, cursor, 'Carlos', 'carlos@example.com', 'senha8765')
# inserir_registro(conexao, cursor, 'Aline', 'aline@example.com', 'pass4321')
# inserir_registro(conexao, cursor, 'Lucas', 'lucas@example.com', '123abc')
# inserir_registro(conexao, cursor, 'Fernanda', 'fernanda@example.com', 'senha789')

# Atualizar um registro
#atualizar_registro(conexao, cursor, 'Rafael bento', 'rbento2024@hotmail.com', '8886652AFG', 6)

# Fechando a conexão com o banco de dados
conexao.close()


