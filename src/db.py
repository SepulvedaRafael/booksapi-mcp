import mariadb
import os
from dotenv import load_dotenv

load_dotenv()

config_no_db = {
    "user": os.getenv("USER_DB"),
    "password": os.getenv("PASSWORD_DB"),
    "host": os.getenv("HOST_DB"),
    "port": int(os.getenv("PORT_DB", "3306"))
}

config_with_db = {
    "user": os.getenv("USER_DB"),
    "password": os.getenv("PASSWORD_DB"),
    "host": os.getenv("HOST_DB"),
    "port": int(os.getenv("PORT_DB", "3306")),
    "database": os.getenv("NAME_DB")
}

name_db = os.getenv("NAME_DB")

conn = None
cursor = None
try:
    conn = mariadb.connect(**config_no_db)
    cursor = conn.cursor()

    create_db_query = f"CREATE DATABASE IF NOT EXISTS {name_db};"
    cursor.execute(create_db_query)
    print(f"Banco de dados '{name_db}' verificado/criado com sucesso!")

    cursor.close()
    conn.close()

    conn = mariadb.connect(**config_with_db)
    print("Conexão estabelecida com sucesso no banco de dados!")
    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS livros (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255),
        year_published INT
    );
    """
    cursor.execute(create_table_query)
    print("Tabela 'livros' criada com sucesso!")
    
except mariadb.Error as e:
    print(f"Erro: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Conexão encerrada.")