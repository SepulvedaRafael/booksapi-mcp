# 🤖 BooksAPI-MCP

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/PYTHON-000000?style=for-the-badge&logo=python&logoColor=facc56" alt="Python"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/FASTAPI-000000?style=for-the-badge&logo=fastapi&logoColor=009688" alt="FastAPI"></a>
<a href="https://modelcontextprotocol.io/docs/getting-started/intro"><img src="https://img.shields.io/badge/MCP-000000?style=for-the-badge&logo=modelcontextprotocol&logoColor=FFFFFF" alt="Model Context Protocol"></a>
<a href="https://code.visualstudio.com/docs/copilot/customization/mcp-servers"><img src="https://img.shields.io/badge/VSCODE-000000?style=for-the-badge" alt="Visual Studio Code"></a>
<a href="hhttps://cursor.com/pt-BR/docs/context/mcp/directory"><img src="https://img.shields.io/badge/CURSOR-000000?style=for-the-badge" alt="Cursor IA"></a>

Esse projeto foi criado por um estudo explorando o Protocolo de Contexto de Modelo (MCP), aplicado em Python e FastAPI, visando entender a sua utilização.

Além disso, ressalta-se que todo o conhecimento adquirido foi por meio de vídeos no Youtube acerca do assunto, mesmo sendo tratado em outras linguagens como Typescript, ainda é útil para entender a sua aplicação em um contexto de Cliente x Servidor.

## 💻 Pré-requisitos
Para adiantar uma etapa, verifique se você possui todos os requisitos:

- Você possui instalado uma versão estável da linguagem `python`.
- Você possui instalado uma versão estável do `git`.
- Você possui instalado um ambiente de desenvolvimento, como `Visual Studio Code` ou outro de sua preferência.

## 🚀 Instalando as dependências
Para instalar as dependências, comece instalando o `pipx`:

```bash
(WINDOWS)
py -m pip install pipx

(LINUX UBUNTU)
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Após isso, realize a instalação do `uv`:
```bash
pipx install uv
```

Em seguida, vá para a pasta que deseja clonar esse repositório e digite:
```bash
git clone https://github.com/SepulvedaRafael/booksapi-mcp.git
```

Após a clonagem, navegue até a pasta que foi gerada e execute cada um dos comandos abaixo:
```bash
uv venv

(WINDOWS)
.venv\Scripts\activate

(LINUX)
source .venv/bin/activate

uv pip install -r pyproject.toml
uv sync
```

## 🔓 Execução do db.py
Para executar os programas corretamente e sem erros, certifique-se de ter o MariaDB Client instalado e que você lembre da suas credenciais. Assim, crie um arquivo com nome .env apenas e adicione:

```bash
USER_DB = root
PASSWORD_DB = password_db
HOST_DB = localhost
PORT_DB = 3306
NAME_DB = booksapi
```

Após essa configuração, basta executar o programa `db.py`.


## 💻 Execução via FastAPI + uvicorn
Para executar esse código via FastAPI e uvicorn, para visualizar ou certificar que a API está funcionando, certifique de estar dentro da pasta /src e executar esse comando:
```bash
uvicorn api:app --reload
```

Caso queira fazer algumas requisições para saber se os endpoints estão funcionando, fique a vontade para executar o comando acima e ir na pasta `requests`. Certifique-se de ter a extensão REST Client (VScode ou Cursor) instalado e clique siga a ordem: POST, GET, PUT e DELETE. Para executar cada um desses arquivos, basta clicar em `Send request`.

## 🤖 Execução via FastMCP + VSCode
Par executar esse código via FastMCP com VSCode, pressione: `CTRL`+ `SHIFT` + `P`. Quando abrir a janela, digite `MCP: Adicionar Servidor`.

Em seguida, clique em Comando (stdio).

A seguir, busque o caminho completo para a pasta /src. Lembre-se que em Windows é `\`.

Como comando do stdio você irá colocar:
```bash
uv --directory <caminho_até_src> run api.py
```

Em seguida, coloque um nome para o seu servidor MCP.

E escolha o tipo de configuração se vai ser Global ou no Workspace. Eu prefiro no Global.

Por fim, você será redirecionado pra basta `mcp.json`, com o código mais ou menos assim:

```json
{
    "servers": {
        "booksapi": {
            "type": "stdio",
            "command": "uv",
            "args": [
                "--directory",
                "<caminho_até_src>",
                "run",
                "api.py"
            ]
        }
    },
    "inputs": []
}
```

Logo acima, terá um botão escrito Início e do lado deveria estar aparecendo 5 ferramentas ou tools. Isso significa que ele reconheceu certinho o seu servidor MCP. Assim, inicie o servidor MCP e caso queira checar está funcionando devidamente, pressione: `CTRL` + `SHIFT` + `U`, isso irá abrir o `OUTPUT` ou `SAÍDA`.

Ao lado do filtro terá uma lista suspensa onde você deverá buscar por: `MCP: nome do seu servidor`. Caso não apareça, vá no arquivo `mcp.json` e clique em `Mais...`, depois vá em `Mostrar saída`.

Para utilizá-lo, basta abrir o Chat, colocar em Agente ao invés de Ask e pressionar na opção que aparece duas ferramentas cruzadas. Nela, deixe selecionado apenas o seu servidor MCP e clique em OK.

Por fim, basta solicitar alguma ação, como adicionar um livro, atualizar algo do livro, deletar o livro, consultar os livros e consultar a quantidade de livros. Quando fizer alguma dessas solicitações, ele irá pedir permissão para cada execução.