import sqlite3
from pathlib import Path

# Definindo o caminho do banco de dados
ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / 'meu_banco.db'

# Conectando ao banco de dados SQLite
conexao = sqlite3.connect(DB_PATH)
cursor = conexao.cursor()

# Definindo a fábrica de linhas para retornar dicionários
cursor.row_factory = sqlite3.Row

# Função para criar a tabela "clientes"
def criar_tabela(conexao, cursor):
    """Cria a tabela 'clientes' caso ainda não exista."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL UNIQUE,
            senha VARCHAR(150) NOT NULL
        )
    ''')
    conexao.commit()

# Função para inserir um registro na tabela "clientes"
def inserir_registro(conexao, cursor, nome, email, senha):
    """Insere um registro na tabela 'clientes'."""
    try:
        cursor.execute("INSERT INTO clientes (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conexao.commit()
    except sqlite3.IntegrityError as e:
        print(f"Erro de integridade: {e}")
        conexao.rollback()
    except Exception as e:
        print(f"Ops! Um erro ocorreu: {e}")
        conexao.rollback()

# Função para atualizar um registro na tabela "clientes"
def atualizar_registro(conexao, cursor, nome, email, senha, id):
    """Atualiza um registro na tabela 'clientes'."""
    try:
        cursor.execute("UPDATE clientes SET nome=?, email=?, senha=? WHERE id=?", (nome, email, senha, id))
        conexao.commit()
    except Exception as e:
        print(f"Ops! Um erro ocorreu: {e}")
        conexao.rollback()

# Função para excluir um registro da tabela "clientes"
def excluir_registro(conexao, cursor, id):
    """Exclui um registro da tabela 'clientes'."""
    try:
        cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
        conexao.commit()
    except Exception as e:
        print(f"Ops! Um erro ocorreu: {e}")
        conexao.rollback()

# Função para autenticar um usuário
def autenticar_usuario(cursor, email, senha):
    """Autentica um usuário com base no email e senha fornecidos."""
    cursor.execute("SELECT * FROM clientes WHERE email=? AND senha=?", (email, senha))
    usuario = cursor.fetchone()
    if usuario:
        print("Autenticação bem-sucedida")
        return True
    else:
        print("Falha na autenticação")
        return False

# Função para inserir múltiplos registros na tabela "clientes"
def inserir_muitos(conexao, cursor, dados):
    """Insere vários registros na tabela 'clientes'."""
    try:
        cursor.executemany("INSERT INTO clientes (nome, email, senha) VALUES (?, ?, ?)", dados)
        conexao.commit()
    except Exception as e:
        print(f"Ops! Um erro ocorreu: {e}")
        conexao.rollback()

# Função para recuperar um cliente pelo ID
def recuperar_cliente(cursor, id):
    """Recupera um cliente pelo ID."""
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

# Função para listar todos os clientes
def listar_clientes(cursor):
    """Lista todos os clientes ordenados por nome."""
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC")

def main():
    # Criar a tabela (caso ainda não exista)
    criar_tabela(conexao, cursor)

    # Inserir alguns registros para teste
    # inserir_registro(conexao, cursor, 'Rafael', 'rafaeltecsuporte@gmail.com', '12345678')
    # inserir_registro(conexao, cursor, 'Ana', 'ana@example.com', 'senha123')

    # Testar a autenticação
    # autenticar_usuario(cursor, 'rafaeltecsuporte@gmail.com', '12345678')
    # autenticar_usuario(cursor, 'ana@example.com', 'senha123')
    # autenticar_usuario(cursor, 'joao@example.com', 'pass123')

    # Recuperar um cliente pelo ID
    cliente = recuperar_cliente(cursor, 2)
    if cliente:
        print(dict(cliente))

    # Listar todos os clientes
    clientes = listar_clientes(cursor)
    for cliente in clientes:
        print(dict(cliente))

    # Fechar a conexão com o banco de dados
    conexao.close()

if __name__ == "__main__":
    main()
