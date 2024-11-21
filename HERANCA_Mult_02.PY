    #  Classe Base / superclasse / classe mae / classe pai 
class Funcionario:
    def trabalhar(self):
        print('Trabalhando....')
    #Herança simples ou Subclasse filha    
class Gerente(Funcionario):
    def trabalhar(self):
        print('Gerenciando....')
        super().trabalhar()
    #Herança simples ou Subclasse filha
class Engenheiro (Funcionario):
    def trabalhar(self):
        print('Enganheando...')
        super().trabalhar()
    # Heranças Multiplas
class LiderTecnico(Gerente, Engenheiro):
    def trabalhar(self):
        print('Liderando')
        super().trabalhar()    
    
    #Instância         
lider_tecnico = LiderTecnico()
lider_tecnico.trabalhar()
print("")    
    #Instância 2  
engenheiro = Engenheiro()
engenheiro.trabalhar()

'''
 
MRO (Método de resolução de Ordem) é a forma de garantir a resolução das classes de heranças multiplas.

'''