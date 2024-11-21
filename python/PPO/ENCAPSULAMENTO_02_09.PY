#%%
'''
INICIA-SE A PROGRAMACAO ORIENTADO A OBJETO
ASSUNTO CLASS.
'''
class Vingador:
    def __init__(self,nome,acessorio,poder,peso): #METODO INICIALIZADOR E CONSTRUTOR
        self.nome = nome
        self.acessorio = acessorio
        self.poder = poder
        self.peso = peso
    
    def mostrar_dados(self): 
        print(f'Nome: {self.nome}')
        print(f'Acessório: {self.acessorio}')
        print(f'Poder: {self.poder}')
        print(f'Peso: {self.peso}')
        
vingador1= Vingador('Tony Stark','Armadura','Da FAMA',87)

vingador1.mostrar_dados()
# %%
'''EXEMPLO PESSOAS'''
class Pessoa:
    # Método COnstrutor
    def __init__(self,nome, sobrenome,idade,cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
    
     
    def __str__(self):
        return f"{self.nome}, {self.sobrenome}, {self.idade}, {self.cidade}"
        
# Criando Instâncias

pessoa1 = Pessoa("Renato","Pordeus Furtado",17,"Kubatão")
pessoa2 = Pessoa("Armando","Guerra",24,"Peruíbe")  
pessoa3 = Pessoa("Zélia","Tokafundo Pinto",70,"Jiparaná")  
pessoa4 = Pessoa("Zita","Rego Xerunda",48,"Xique - Xique")  
pessoa5 = Pessoa("Otávio","Bundovsky",19,"Rolândia")  
pessoa6 = Pessoa("Nazaré","Tedesco",63,"Paulo Afonso")  

print("\n")
print("Participantes de Reality CASA DOS DESASTRES\n")
print(f"Participante 1: {pessoa1}")
print(f"Participante 2: {pessoa2}")
print(f"Participante 3: {pessoa3}")
print(f"Participante 4: {pessoa4}")
print(f"Participante 5: {pessoa5}")
print(f"Participante 6: {pessoa6}")

# %%
''' ENCAPSULAMENTO: PODE SER ATRIBUTOS PRIVADO OU PUBLICO,'''

class Pessoas:
    def __init__(self, nome, email, senha):
        self.nome = nome  # Atributo público
        self.email = email  # Atributo público
        self.__senha = senha  # Atributo privado
        
    def mostrar_senha(self):
        return self.__senha  # Método público para acessar o atributo privado
        
    def mostrar_nome(self):
        return self.nome
    
    def mostrar_email(self):
        return self.email
    
user = Pessoas('Facebookson da Silva Junior Neto', 'facebookson@google.com', 'admin')
user2 = Pessoas('Jacinto Alegria Matinal', 'Jacinto@alegria.com.br', 'Ademin')
print(f'Nome: {user.nome}\n')
print(f'Email: {user.email}\n')

try:
    print(f'Senha: {user.__senha}\n')  # Isto irá gerar um erro
except AttributeError:
    print(f'O atributo não é acessível diretamente\n')

print(f'Nome (usando método): {user.mostrar_nome()}\n')
print(f'Email (usando atributo): {user.email}\n')
print(f'Senha (usando método): {user.mostrar_senha()}\n')

print(f'Nome (usando método): {user2.mostrar_nome()}\n') # <-- Usuario 2 forma de acessar
print(f'Email (usando método): {user2.mostrar_email()}\n') # <-- Usuario 2 forma de acessar
print(f'Senha (usando método): {user2.mostrar_senha()}\n') # <-- Usuario 2 forma de acessar

# %%
''' Encapsulamento 2.0'''

class Pessoas:
    def __init__(self, nome, email, senha):
        self._nome = nome  # Atributo Protegido
        self._email = email  # Atributo Protegido
        self.__senha = senha  # Atributo privado

    ''' Metodos de acessar os atributos privados com metodo Publico'''
    @property # <-- Metodo get em JAVA
    def nome(self):
        return self._nome
    
    @nome.setter # <-- Metodo set em JAVA
    def nome(self,valor):
        self._nome = valor
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,valor):
        self._email = valor
    
    @property
    def senha(self):
        return self.__senha
        
    def mostrar_senha(self):
        return self.__senha  # Método público para acessar o atributo privado
        
    def mostrar_nome(self):
        return self._nome
    
    def mostrar_email(self):
        return self._email

user = Pessoas('Facebookson da Silva Junior Neto', 'facebookson@google.com', 'admin')
user2 = Pessoas('Jacinto Alegria Matinal', 'Jacinto@alegria.com.br', 'Ademin')

print(f'Nome: {user.nome}')
# %%
