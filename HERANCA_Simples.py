'''
HERANCA
classes e sub-classes

'''

#classe base (SuperClasse / Classe mae / Classe Pai)

class Vigadores: 
    def __init__(self, nome, poder): #Metodo construtor
        self.nome = nome # Atributos
        self.poder = poder # Atributos
        
    def apresentar(self): # Metodo
        return f'{self.nome}, com o poder de {self.poder} '
        

# Sub-classe( ou Classe filha)
class Heroi(Vigadores): # sub-class
    def __init__(self, nome, poder, identidade_secreta): # metodo construtor da class filha
        super().__init__(nome, poder) # Super é a funcao de trazer as informacoes ja escrita na classe acima.
        self.identidade_secreta = identidade_secreta

    # Polimorfismo
    def apresentar(self):
        return f'{super().apresentar()} e identidade secreta: {self.identidade_secreta}'

# outra sub-classe da SuperClasse.
class Vilao(Vigadores):

    def __init__(self, nome, poder, plano): # metodo construtor da class filha
        super().__init__(nome, poder)
        self.plano = plano # novo atributo dessa sub-classe 
    
    # Polimorfismo
    def apresentar(self):
        return f'{super().apresentar()}, e seu Plano é: {self.plano}'    
    
# Criando as Instancias (objetos) 
iron_men = Heroi('Homem de Ferro', 'Tecnologia de armadura', 'Tonny Star')
Thannos = Vilao('thannos da silva Junior Neto', ' Fazer bolinha de sabao', 'Dominar o universo')

# usando os metodos
print(f'Criando um Heroi \n\n{iron_men.apresentar()} \n\nCriando um Vilao\n')
print(Thannos.apresentar())