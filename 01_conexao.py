import sqlite3
from pathlib import Path

# Definindo o caminho do banco de dados
ROOT_PATH = Path(__file__).parent
# Conectando ao banco de dados SQLite
conexao = sqlite3.connect(ROOT_PATH / 'meu_banco.db')
# Criando um cursor para interagir com o banco de dados
cursor = conexao.cursor()

# Criando a tabela "clientes"
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

# Dados a serem inseridos
data = ("Rafael", "rafaeltecsuporte@gmail.com", "12345678")
# Inserindo os dados na tabela "clientes"
cursor.execute("INSERT INTO clientes (nome, email, senha) VALUES (?, ?, ?)", data)

# Confirmando as mudanças
conexao.commit()

# Fechando a conexão com o banco de dados
conexao.close()
