from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv() # carrega o arquivo com as variaveis de ambiente

# Função para conectar ao banco de dados Neo4j
def connect_to_neo4j(uri, username, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        return driver
    except Exception as e:
        print("Erro ao conectar ao Neo4j:", e)
        return None

# Função para criar uma pessoa
def criar_pessoa(session, nome, idade):
    query = "CREATE (n:pessoa {name: $nome, idade: $idade})"
    session.run(query, nome=nome, idade=idade)
    print(f"Pessoa '{nome}' criada!")

# Função para criar um relacionamento
def criar_relacionamento(session, nome1, nome2, relacionamento):
    query = f"""
    MATCH (a:pessoa {{name: $nome1}}), (b:pessoa {{name: $nome2}})
    CREATE (a)-[:{relacionamento}]->(b)
    RETURN a, b
    """
    session.run(query, nome1=nome1, nome2=nome2)

def 

# Parâmetros de conexão
uri = "neo4j+s://fd936d1c.databases.neo4j.io"  # URI do seu servidor Neo4j
username = os.getenv('username')  # Nome de usuário do Neo4j
password = os.getenv('password')  # Senha do Neo4j

# Tentar conectar ao banco de dados
driver = connect_to_neo4j(uri, username, password)

# Verificar se a conexão foi bem-sucedida
if driver:
    session = driver.session()  # Cria uma sessão para usar no loop
    try:
        while True:
            opcao = input('Escolha uma operação: 1 (criar pessoa)\n2 (criar relacionamento)\n0 (sair): ')
            match opcao:
                case '1':
                    nome = input('Digite o nome da pessoa: ')
                    idade = input('Digite a idade da pessoa: ')
                    criar_pessoa(session, nome, idade)
                case '2':
                    nome1 = input('digite o primeiro nome:')
                    nome2 = input('digite o segundo nome:')
                    relacionamento = input('digite o nome do relacionamento:')
                    criar_relacionamento(session,nome1,nome2,relacionamento)
                case '0':
                    break
    finally:
        session.close()  # Fecha a sessão após o loop
        driver.close()    # Fecha o driver completamente após o uso
else:
    print("Não foi possível conectar ao banco de dados.")
