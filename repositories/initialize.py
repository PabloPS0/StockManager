"""
This module is responsible for the creation and initial configuration of the SQLite database and the necessary 
directories for data storage. It uses environment variables to determine the database path and automatically 
creates the folder for the database if it doesn't exist. 
"""
import os
import sqlite3
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Obtém os caminhos do banco de dados das variáveis de ambiente
DATABASE_PATH = os.getenv("DATABASE_PATH")

# Define o diretório e caminho completo dos bancos de dados
DB_FOLDER = os.path.dirname(DATABASE_PATH)
DB_PATH = os.path.join(DB_FOLDER, "database.db")

# Cria os diretórios para os bancos de dados, caso não existam
os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)

def create_table(cursor, create_table_query, table_name):
    """
    Cria a tabela no banco de dados, se não existir, e confirma as alterações.
    """
    try:
        cursor.execute(create_table_query)
        cursor.connection.commit()  # Confirma as alterações
        print(f"Tabela '{table_name}' criada ou já existe.")
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela '{table_name}': {e}")

# Conectar-se aos bancos de dados
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Definindo as consultas de criação das tabelas
create_users_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
'''

create_products_table_query = '''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL CHECK (price > 0 AND price == ROUND(price, 2)),
        quantity INTEGER NOT NULL CHECK (quantity >= 0),
        image_url TEXT,
        category TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
'''

# Criando as tabelas
create_table(cursor, create_users_table_query, "users")
create_table(cursor, create_products_table_query, "products")

# Fechando as conexões
conn.close()
