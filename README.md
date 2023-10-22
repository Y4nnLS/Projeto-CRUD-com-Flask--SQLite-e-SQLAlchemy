<h1 align='center'>
    <p>Projeto CRUD com Flask, SQLite e SQLAlchemy</p>
</h1>

## 🙋‍♂️ Equipe de desenvolvedores
<p>Felipe Franco Pinheiro</p>
<p>Yann Lucas Saito da Luz</p>

## 📘 Sobre

Este projeto é uma aplicação web Flask para gerenciar uma base de dados de energéticos. Ele permite adicionar, listar, atualizar e excluir entradas de energéticos no banco de dados.

Requerimentos:
- Flask
- Flask-SQLAlchemy

#### Uso:
    1. O programa permite o cadastro de energéticos em um banco de dados.
    2. Permite ao usuário cadastrar, alterar e visualizar os itens no banco de dados.

## Estrutura do Projeto
A estrutura do projeto é composta pelos seguintes arquivos e diretórios:

- app.py: O arquivo principal que contém a aplicação Flask e as definições de rotas.
- templates/: Diretório contendo os templates HTML usados para renderizar as páginas.
- exemplo.db: O arquivo do banco de dados SQLite onde os dados dos energéticos são armazenados.

## Funcionalidades:
- `@app.route('/')`: Exibe uma lista de todos os energéticos no banco de dados.
- `@app.route('/inserir', methods=['POST'])` : Permite adicionar um novo energético ao banco de dados.
- `@app.route('/excluir/<int:id>')`: Permite excluir um energético do banco de dados.
- `@app.route('@app.route('/atualizar/<int:id>', methods=['GET','POST'])')`: Permite atualizar as informações de um energético no banco de dados.
- `@app.route('@app.route('/listar', methods=['POST'])')`: Exibe uma lista de energéticos de uma marca específica.

## Classe Energetico: 
Representa um energético no banco de dados.

#### Atributos:

- id (int): Identificador único do energético.
- nome (str): Nome do energético.
- tamanho_lata (int): Tamanho da lata em mililitros.
- sabor (str): Sabor do energético.
- marca (str): Marca do energético.
- preco (float): Preço do energético.

## Funcionamento Interno

O projeto utiliza o SQLAlchemy como ORM para lidar com o banco de dados. A aplicação Flask é configurada para utilizar um banco de dados SQLite.

## 📝 Ferramentas

- [Python](https://docs.python.org/3/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)

## Comandos

<p> instala todas as dependências listadas em requirements.txt :</p>

    pip install -r requirements.txt    

<p> lista os modulos disponíveis : </p> 

    pip list 

