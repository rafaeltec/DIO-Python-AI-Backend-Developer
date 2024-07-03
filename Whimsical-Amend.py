import sqlite3
from pathlib import Path

# Definindo o caminho do banco de dados
ROOT_PATH = Path(__file__).parent
DB_PATH = ROOT_PATH / 'Whimsical-Amend.db'

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