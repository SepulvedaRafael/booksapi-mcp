import mariadb
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from typing import Any

load_dotenv()

mcp = FastMCP("booksAPI")

config = {
    "user": os.getenv("USER_DB"),
    "password": os.getenv("PASSWORD_DB"),
    "host": os.getenv("HOST_DB"),
    "port": int(os.getenv("PORT_DB", "3306")),
    "database": os.getenv("NAME_DB")
}

def adicionar_livro(livro: dict[str, Any]) -> dict[str, str]:
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()

        add_book_query = "INSERT INTO livros (title, author, year_published) VALUES (?, ?, ?)"
        values = (livro['title'], livro['author'], livro['year_published'])

        cursor.execute(add_book_query, values)
        conn.commit()

        return {"mensagem": f"Livro '{livro['title']}' adicionado com sucesso!"}

    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao adicionar o livro: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def atualizar_livro(livro: dict[str, Any], id: int) -> dict[str, str]:
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        
        update_book_query = "UPDATE livros SET title = ?, author = ?, year_published = ? WHERE id = ?"
        values = (livro['title'], livro['author'], livro['year_published'], id)
        
        cursor.execute(update_book_query, values)
        conn.commit()
        
        return {"mensagem": f"Livro '{livro['title']}' atualizado com sucesso!"}
    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar o livro: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def remover_livro(id: int) -> dict[str, str]:
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        
        select_book_query = "SELECT title FROM livros WHERE id = ?"
        cursor.execute(select_book_query, (id,))
        livro = cursor.fetchone()

        if livro is None:
            raise HTTPException(status_code=404, detail=f"Livro com ID {id} não encontrado.")

        delete_book_query = "DELETE FROM livros WHERE id = ?"
        cursor.execute(delete_book_query, (id,))
        conn.commit()
        
        return {"mensagem": f"Livro '{livro[0]}' removido com sucesso!"}

    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao remover o livro: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def qtd_livros() -> dict[str, int]:
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()

        count_books_query = "SELECT COUNT(*) FROM livros"
        cursor.execute(count_books_query)
        (count,) = cursor.fetchone()

        return {"quantidade_livros": count}

    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao contar os livros: {e}")

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def consultar_todos_livros() -> list[dict[str, Any]]:
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        
        select_all_books_query = "SELECT * FROM livros"
        cursor.execute(select_all_books_query)

        colunas = [i[0] for i in cursor.description]

        books_tuples : list[tuple[str, Any]] = cursor.fetchall()
        books_dicts : list[dict[str, Any]] = [dict(zip(colunas, book)) for book in books_tuples]
        
        return books_dicts
        
    except mariadb.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar todos os livros: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

app = FastAPI()

class Livro(BaseModel):
    title: str
    author: str
    year_published: int

@mcp.tool()
@app.post("/livros")
async def criar_livro(livro: Livro) -> dict[str, str]:
    """
    Endpoint para adicionar um novo livro ao banco de dados.
    """
    try:
        resultado = adicionar_livro(livro.dict())
        return resultado
    except HTTPException as e:
        raise e

@mcp.tool()
@app.get("/quantidade")
async def quantidade_livros() -> dict[str, int]:
    """
    Endpoint para obter a quantidade de livros no banco de dados.
    """
    try:
        resultado = qtd_livros()
        return resultado
    except HTTPException as e:
        raise e

@mcp.tool()
@app.get("/")
async def consultar_livros() -> list[dict[str, Any]]:
    """
    Endpoint para consultar todos os livros no banco de dados.
    """
    try:
        resultado = consultar_todos_livros()
        return resultado
    except HTTPException as e:
        raise e

@mcp.tool()
@app.put("/livros/{id}")
async def atualizar_livro_api(id: int, livro: Livro) -> dict[str, str]:
    """
    Endpoint para atualizar um livro no banco de dados.
    """
    try:
        resultado = atualizar_livro(livro.dict(), id)
        return resultado
    except HTTPException as e:
        raise e

@mcp.tool()
@app.delete("/livros/{id}")
async def remover_livro_api(id: int) -> dict[str, str]:
    """
    Endpoint para remover um livro no banco de dados.
    """
    try:
        resultado = remover_livro(id)
        return resultado
    except HTTPException as e:
        raise e

if __name__ == "__main__":
    mcp.run(transport="stdio")