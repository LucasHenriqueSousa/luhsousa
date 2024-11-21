'''

DDL - Data Definition Language
A Linguagem de Definição de Dados (DDL) é utilizada para definir e modificar a estrutura dos bancos de dados. Ela permite criar, alterar ou excluir tabelas, bancos de dados e índices. 

######Os principais comandos DDL são:######

CREATE: cria novas tabelas, índices ou bancos de dados.
ALTER: modifica a estrutura existente de uma tabela ou banco de dados, como adicionar ou remover colunas.
DROP: remove uma tabela, banco de dados ou índice.
Exemplos de uso:

-- Criar uma tabela de usuários
CREATE TABLE usuarios (
    id INT,
    nome VARCHAR(50),
    email VARCHAR(100)
);

-- Alterar a tabela adicionando uma nova coluna
ALTER TABLE usuarios ADD data_nascimento DATE;

-- Excluir a tabela
DROP TABLE usuarios;
DML - Data Manipulation Language



A Linguagem de Manipulação de Dados (DML) é usada para manipular os dados armazenados em tabelas, permitindo realizar operações de inserção, leitura, atualização e exclusão de registros. As principais operações DML incluem:

INSERT INTO: insere novos registros.
UPDATE: atualiza registros existentes.
DELETE: remove registros.
Essas operações formam o modelo CRUD (Create, Read, Update, Delete), que descreve o ciclo básico de manipulação de dados.

Exemplos de uso:


-- Inserir um novo registro na tabela de usuários
INSERT INTO usuarios (id, nome, email) 
VALUES (1, 'João Silva', 'joao@example.com');

-- Atualizar o e-mail de um usuário específico
UPDATE usuarios 
SET email = 'joao.novo@example.com' 
WHERE id = 1;

-- Excluir um registro da tabela de usuários
DELETE FROM usuarios 
WHERE id = 1;
DQL - Data Query Language




A Linguagem de Consulta de Dados (DQL) é usada para recuperar informações das tabelas. Seu principal comando é o SELECT, 
que pode ser complementado com cláusulas e funções agregadas para filtrar, agrupar e organizar os resultados. 


Algumas das principais características incluem:

Funções agregadas como COUNT, AVG, SUM, MAX, MIN para realizar cálculos.
Cláusulas como ORDER BY para ordenar, GROUP BY para agrupar, HAVING para filtrar grupos e IN/NOT IN para verificar se valores pertencem ou não a um conjunto específico.
Exemplos de uso:

-- Contar o número total de usuários
SELECT COUNT(*) 
FROM usuarios;

-- Calcular a média de salários de funcionários
SELECT AVG(salario) 
FROM funcionarios;

-- Agrupar vendedores por nome e somar suas vendas, filtrando aqueles com mais de 1000 vendas
SELECT nome, SUM(vendas) 
FROM vendedores 
GROUP BY nome 
HAVING SUM(vendas) > 1000;

-- Selecionar produtos de categorias específicas
SELECT * 
FROM produtos 
WHERE categoria IN ('Eletrônicos', 'Móveis');

'''

import sqlite3

# criar uma funcao para conectar ao banco de dados

def connect():
    return sqlite3.connect('crud_exemple.db')
#fUNCAO PARA CRIAR A TABELA
def create_table():
    with connect()as conn:
        cursor = conn.cursor()
        # DDL esta parte abaixo
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS aluno(                
            id_user INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL, 
            idade INTEGER NOT  NULL, 
            
        )
                       ''')
    conn.commit()

#funcao para criar aluno

def create_student(nome, idade):
    with connect()as conn:
        cursor = conn.cursor()
        # DML esta parte abaixo
        cursor.execute(''' 
        INSERT INTO Usuario (nome, idade) VALUES(?,?) 
        ''', (nome,idade))
        conn.commit()   # USAMOS o CONN.COMMIT QUANDO IREMOS ALTERAR OU CRIAR TABELAS 
#Funcao para leitura
def read_student():
    with connect()as conn:
        cursor = conn.cursor()
        # Aqui é DQL
        cursor.execute('SELECT * FROM aluno')
        return cursor.fetchall() # SOMENTE QUANDO IREMOS FAZER LEITURA DOS VALORES DA TABELA USAMOS O FETCHALL()


# Funcao para atualizar minha tabela aluno

def update_student(student_id, nome, idade):
    with connect()as conn:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE aluno SET nome = ?, idade = ? WHERE id =?
        ''', (nome,idade,student_id))
        conn.commit()

# funcao para deletar alunos

def delete_student(student_id):
    with connect()as conn:
        cursor = conn.cursor()
        # Aqui usamos o DML
        cursor.execute('DELETE FROM aluno WHERE id = ?', (student_id,))
        conn.commit()
        
# USO DO CRUD
if __name__ == '__main__':
    create_table() #Cria a tabela se nao existir
    
    #CRIAR ALUNOS
    
    create_student('Lucas', 29)
    create_student('Adelina', 800)
    create_student('Samila', 15)
    create_student('Debora', 24)
    create_student('Jackeline', 34)
    
    #Ler os usuarios 
    print('Usuario após a criacao:')
    print(read_student())
    
    # atualizar o usuario
    
    update_student(2, 'Lucréia', 11)
    
    print('Usuario após update:')
    print(read_student())
    
    
    # Deletar o usuario
    delete_student(3)
    
    print('Usuario após o delete:')
    print(read_student())
    