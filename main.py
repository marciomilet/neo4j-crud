from neo4j import GraphDatabase

# Função para conectar ao banco de dados Neo4j
def connect_to_neo4j(uri, username, password):
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        session = driver.session()
        return session
    except Exception as e:
        print("Erro ao conectar ao Neo4j:", e)
        return None

# Parâmetros de conexão
uri = "neo4j+s://fd936d1c.databases.neo4j.io"  # URI do seu servidor Neo4j
username = "neo4j"  # Nome de usuário do Neo4j
password = "sua_senha"  # Senha do Neo4j

# Tentar conectar ao banco de dados
session = connect_to_neo4j(uri, username, password)

# Verificar se a conexão foi bem-sucedida
if session:
    print("Conexão com o Neo4j estabelecida com sucesso!")
    # Você pode executar consultas aqui
    # Exemplo: session.run("MATCH (n) RETURN count(n)")
    session.close()  # Não se esqueça de fechar a sessão quando terminar
else:
    print("Não foi possível estabelecer conexão com o Neo4j.")