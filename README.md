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
(WINDOWS)
pipx install uv

(LINUX UBUNTU)
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
.venv/Scripts/activate

(LINUX)
source .venv/bin/activate

uv pip install -r pyproject.toml
uv sync
```

> [!IMPORTANT]
> Execute cada linha individualmente e certifique que a instalação foi realizada com sucesso.